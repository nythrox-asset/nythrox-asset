# -*- coding: utf-8 -*-
"""Monte le serveur Discord de support Nythrox sur un serveur DEJA cree.

Pourquoi ce script ne cree pas le serveur lui-meme
--------------------------------------------------
L'API permet a un bot de creer un serveur, mais le bot en devient alors le
PROPRIETAIRE. Pour un serveur de support commercial c'est un piege : le
transfert de propriete vers un humain est une action de compte protegee par la
double authentification, qu'un bot ne peut pas faire a ta place. Tu crees donc
le serveur vide toi-meme, en deux clics, et ce script pose tout le reste.

Ce qu'il fait
-------------
Roles, categories, salons (dont deux forums et une categorie STAFF privee),
permissions, balises de forum, message d'accueil, et l'activation du mode
COMMUNAUTE. Idempotent : il compare par NOM et ne recree jamais ce qui existe
deja, donc tu peux le relancer sans crainte apres un echec.

Ce qu'il change dans les REGLAGES de ton serveur
------------------------------------------------
L'activation du mode Communaute impose deux minimums a Discord, que le script
applique donc : niveau de verification sur "email verifie", et filtre de
contenu explicite sur "tous les membres". Ce sont des exigences de Discord,
pas un choix : sans elles, l'API refuse d'activer le mode.

Preparation, une seule fois
---------------------------
1. Cree le serveur dans Discord : bouton `+`, Creer mon propre serveur.
2. https://discord.com/developers/applications, New Application, onglet Bot,
   Reset Token, copie le jeton.
3. Onglet OAuth2 > URL Generator : scope `bot`, permission `Administrator`.
   Ouvre l'URL generee et invite le bot sur TON serveur.
4. Recupere l'identifiant du serveur : Discord > Parametres avances > active
   le Mode developpeur, puis clic droit sur le serveur > Copier l'ID.

Utilisation
-----------
Le jeton n'est JAMAIS ecrit dans un fichier ni passe en argument, il transite
par une variable d'environnement, et c'est TOI qui lances la commande :

    $env:DISCORD_BOT_TOKEN = "colle_ton_jeton_ici"
    $env:DISCORD_GUILD_ID  = "1531090209855246386"
    python scripts/monter_discord_support.py            # montre le plan
    python scripts/monter_discord_support.py --apply    # applique

Sans --apply, il n'ecrit rien : il affiche ce qu'il ferait.
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request

API = "https://discord.com/api/v10"

# Types de salon Discord.
CATEGORIE, TEXTE, ANNONCE, FORUM = 4, 0, 5, 15

# Bits de permission utiles.
VIEW_CHANNEL = 1 << 10
SEND_MESSAGES = 1 << 11
MANAGE_MESSAGES = 1 << 13
MENTION_EVERYONE = 1 << 17
MANAGE_THREADS = 1 << 34

# --------------------------------------------------------------------------
# Le plan. Modifie ICI si tu veux une autre structure.
# --------------------------------------------------------------------------
# (nom, type, sujet, diffusion, prive)
#   diffusion : @everyone lit mais n'ecrit pas.
#   prive     : @everyone ne voit meme pas le salon, seul le role Nythrox.
PLAN = [
    ("INFORMATION", [
        # #welcome reste un salon TEXTE, meme en mode Communaute : c'est lui
        # qui sert de salon de REGLES, et Discord attend un salon texte
        # ordinaire a cet endroit. Personne ne s'abonne a des regles.
        ("welcome", TEXTE, "Rules and how to ask for help", True, False),
        ("announcements", ANNONCE, "Releases and important news", True, False),
        ("changelog", ANNONCE, "One entry per published version", True, False),
    ]),
    ("SUPPORT", [
        ("support-en", TEXTE, "Support in English", False, False),
        ("support-fr", TEXTE, "Support en francais", False, False),
        ("bug-reports", FORUM, "One thread per bug", False, False),
        ("feature-requests", FORUM, "One thread per idea", False, False),
    ]),
    ("COMMUNITY", [
        # #showcase = ce que les ACHETEURS construisent avec les packs, pas la
        # vitrine de Nythrox. A ne pas confondre avec le site nythrox-asset.com
        # ni avec le lien "Showcase Video" des fiches Fab.
        ("showcase", TEXTE, "Show what you built with Nythrox packs", False, False),
        ("general", TEXTE, "Anything else", False, False),
    ]),
    ("STAFF", [
        # Salon des avis de moderation de Discord. Il DOIT exister pour que le
        # mode Communaute s'active, et il doit rester prive : Discord y depose
        # des alertes qui te sont destinees, pas a tes acheteurs.
        ("server-updates", TEXTE, "Discord moderation notices, staff only",
         False, True),
        # Transcriptions des tickets fermes. A renseigner dans Ticket Tool,
        # sinon tu perds l'historique des le premier ticket ferme.
        ("ticket-logs", TEXTE, "Ticket transcripts, staff only", False, True),
    ]),
]

# Balises du forum des bugs. Un forum sans balises redevient un salon en vrac.
BALISES_BUGS = ["Door System", "Selection & Assembly", "Asset pack",
                "Confirmed", "Fixed", "Not reproducible"]
BALISES_IDEES = ["Door System", "Selection & Assembly", "Asset pack",
                 "Planned", "Declined"]

ROLES = [
    # (nom, couleur, mentionnable, affiche_separement)
    # Nythrox : ton role de staff. Affiche a part dans la liste des membres,
    # pour qu'un acheteur voie immediatement qui repond officiellement.
    ("Nythrox", 0x1D4ED8, False, True),
    # Verified buyer : attribue a la main apres verification de la commande
    # Fab. C'est lui qui justifie une reponse prioritaire.
    ("Verified buyer", 0x3B82F6, False, True),
    # Member : role neutre, utile le jour ou tu voudras restreindre un salon
    # sans toucher a @everyone. Sans couleur ni mise en avant.
    ("Member", 0x000000, False, False),
]

# --------------------------------------------------------------------------
# AutoMod. Quatre regles, pas trente : chaque regle en trop finit par bloquer
# un acheteur de bonne foi, et c'est toi qui passes ensuite dix minutes a
# comprendre pourquoi son message n'est jamais arrive.
#
# Valeurs de l'API, verifiees sur la documentation Discord du 27/07/2026
# (docs.discord.com/developers/resources/auto-moderation), parce que de
# memoire je les avais fausses :
#   trigger_type  1 = KEYWORD, 3 = SPAM, 4 = KEYWORD_PRESET,
#                 5 = MENTION_SPAM, 6 = MEMBER_PROFILE
#   action.type   1 = bloquer le message, 2 = alerter dans un salon,
#                 3 = exclusion temporaire, 4 = blocage des interactions
# Il n'existe AUCUN declencheur "lien d'invitation" : ca se fait avec une
# regle a mots-cles et une expression reguliere.
#
# Quotas par serveur : 6 regles KEYWORD, 1 SPAM, 1 MENTION_SPAM. On en
# consomme 2 sur 6, 1 sur 1 et 1 sur 1.
# --------------------------------------------------------------------------
MOTS_PIRATAGE = ["free download", "cracked", "torrent", "nulled",
                 "keygen", "warez"]

# `(?i)` rend l'expression insensible a la casse. Pas de lookahead ni de
# lookbehind : le moteur de Discord est celui de Rust, qui ne les gere pas.
INVITATIONS = [
    r"(?i)discord(app)?\.(gg|com/invite|me)/[a-z0-9_-]+",
    r"(?i)(dsc|invite)\.gg/[a-z0-9_-]+",
]

AUTOMOD = [
    # (nom, trigger_type, trigger_metadata, alerter, explication)
    #
    # Le demarchage par invitation est le premier parasite d'un serveur de
    # support qui commence a etre visible.
    ("Nythrox - pas d'invitations", 1, {"regex_patterns": INVITATIONS}, True,
     "bloque les invitations vers d'autres serveurs"),
    # Regle integree, entrainee par Discord sur son propre trafic. Rien a
    # regler, et elle attrape ce qu'une liste de mots ne verra jamais.
    ("Nythrox - anti-spam", 3, None, False,
     "bloque le spam, detection integree de Discord"),
    # Le piratage se demande presque toujours avec les memes mots. On bloque
    # le message ET on t'alerte : celui qui demande revient souvent.
    ("Nythrox - pas de piratage", 1, {"keyword_filter": MOTS_PIRATAGE}, True,
     "bloque les demandes de version piratee et t'alerte"),
    # Une vague de mentions est la facon la plus simple de pourrir un serveur
    # ouvert. Cinq personnes citees dans un message suffisent largement pour
    # du support.
    ("Nythrox - vagues de mentions", 5, {"mention_total_limit": 5}, True,
     "bloque les messages citant plus de 5 personnes"),
]

ACCUEIL = """**Welcome to Nythrox.**
Environments, modular kits and tools for Unreal Engine.

**Need help?** Post in #support-en or #support-fr.
Found a bug? Open a thread in #bug-reports.

**To get a useful answer on the first try, include:**
- your Unreal Engine version, and the exact product version
- what you did, what you expected, what happened instead
- a screenshot, and the Output Log if something failed
- whether it also happens in a brand new empty project

**House rules**
1. One topic per thread. It keeps answers findable for the next person.
2. No piracy, no asking for or sharing purchased files. Instant ban.
3. Be civil. Nobody here owes you anything.
4. Custom development requests go to DM, not the support channels.

Typical first answer within 48h, weekends included but slower."""


def appel(methode, chemin, jeton, charge=None):
    """Un appel API, avec respect du rate limit de Discord."""
    donnees = json.dumps(charge).encode("utf-8") if charge is not None else None
    requete = urllib.request.Request(API + chemin, data=donnees, method=methode)
    requete.add_header("Authorization", "Bot " + jeton)
    requete.add_header("Content-Type", "application/json")
    requete.add_header("User-Agent", "NythroxSupportSetup/1.0")
    try:
        with urllib.request.urlopen(requete) as reponse:
            corps = reponse.read().decode("utf-8")
            return json.loads(corps) if corps else {}
    except urllib.error.HTTPError as erreur:
        detail = erreur.read().decode("utf-8", "replace")
        if erreur.code == 429:
            # Discord demande d'attendre : on attend et on retente une fois.
            attente = 5.0
            try:
                attente = float(json.loads(detail).get("retry_after", 5.0))
            except Exception:  # noqa: BLE001
                pass
            print("   rate limit, pause de %.1fs" % attente)
            time.sleep(attente + 0.5)
            return appel(methode, chemin, jeton, charge)
        raise SystemExit(
            "Discord a refuse %s %s : %s\n%s"
            % (methode, chemin, erreur.code, detail))


def main(argv):
    appliquer = "--apply" in argv
    jeton = os.environ.get("DISCORD_BOT_TOKEN", "").strip()
    guilde = os.environ.get("DISCORD_GUILD_ID", "").strip()
    if not jeton or not guilde:
        raise SystemExit(
            "Il manque DISCORD_BOT_TOKEN ou DISCORD_GUILD_ID.\n"
            "Voir l'en-tete de ce fichier pour la preparation.")

    if not appliquer:
        print("MODE PLAN, rien ne sera ecrit. Ajoute --apply pour appliquer.\n")

    infos = appel("GET", "/guilds/%s" % guilde, jeton)
    print("serveur : %s" % infos.get("name"))

    # Les salons d'ANNONCES (type 5) n'existent que sur un serveur en mode
    # Communaute. Sur un serveur ordinaire, Discord refuse la creation avec
    # 50035 "Value must be one of {0, 2, 4, 6, 13, 14, 15, 16}" : le type 5
    # est absent de la liste, le 15 (forum) y est. Plutot que d'echouer au
    # troisieme salon en laissant le serveur a moitie monte, on detecte et on
    # retombe sur des salons texte, qui se convertissent en un clic apres coup.
    communaute = "COMMUNITY" in (infos.get("features") or [])
    if communaute:
        print("mode    : Communaute active, salons d'annonces disponibles\n")
    else:
        print("mode    : serveur ORDINAIRE\n"
              "          Les salons d'annonces ne sont pas disponibles ; ils\n"
              "          seront crees en salons TEXTE, ce qui ne change rien\n"
              "          a leur usage ni a leurs permissions.\n"
              "          Pour les vrais salons d'annonces, auxquels les gens\n"
              "          peuvent s'abonner : Parametres du serveur > Activer\n"
              "          le mode Communaute, puis relance ce script.\n")

    existants = appel("GET", "/guilds/%s/channels" % guilde, jeton)
    par_nom = {c["name"]: c for c in existants}
    roles_existants = {r["name"]: r
                       for r in appel("GET", "/guilds/%s/roles" % guilde, jeton)}
    everyone = roles_existants.get("@everyone", {}).get("id", guilde)

    # --- roles ---------------------------------------------------------
    for nom, couleur, mentionnable, en_avant in ROLES:
        if nom in roles_existants:
            print("role      %-22s deja present" % nom)
            continue
        print("role      %-22s A CREER" % nom)
        if appliquer:
            roles_existants[nom] = appel(
                "POST", "/guilds/%s/roles" % guilde, jeton,
                {"name": nom, "color": couleur,
                 "mentionable": mentionnable, "hoist": en_avant})
            time.sleep(0.3)

    # L'identifiant du role de staff sert a ouvrir les salons prives. Le
    # proprietaire du serveur les voit de toute facon, mais le jour ou tu
    # ajoutes quelqu'un, il suffira de lui donner ce role.
    staff = roles_existants.get("Nythrox", {}).get("id")

    # --- categories et salons -------------------------------------------
    for categorie, salons in PLAN:
        parent = par_nom.get(categorie)
        if parent:
            print("categorie %-22s deja presente" % categorie)
        else:
            print("categorie %-22s A CREER" % categorie)
            if appliquer:
                parent = appel("POST", "/guilds/%s/channels" % guilde, jeton,
                               {"name": categorie, "type": CATEGORIE})
                par_nom[categorie] = parent

        for nom, type_salon, sujet, diffusion, prive in salons:
            if nom in par_nom:
                print("  salon   %-22s deja present" % nom)
                continue
            type_effectif = (TEXTE if type_salon == ANNONCE and not communaute
                             else type_salon)
            etiquette = {ANNONCE: "annonce", FORUM: "forum",
                         TEXTE: "texte"}[type_effectif]
            if prive:
                etiquette += ", prive"
            print("  salon   %-22s A CREER (%s)" % (nom, etiquette))
            if not appliquer:
                continue
            charge = {"name": nom, "type": type_effectif, "topic": sujet}
            if parent:
                charge["parent_id"] = parent["id"]
            if prive:
                # Salon prive : @everyone ne le voit pas du tout.
                charge["permission_overwrites"] = [
                    {"id": everyone, "type": 0, "deny": str(VIEW_CHANNEL)}]
                if staff:
                    charge["permission_overwrites"].append(
                        {"id": staff, "type": 0, "allow": str(VIEW_CHANNEL)})
            elif diffusion:
                # Salon de diffusion : @everyone lit mais n'ecrit pas.
                charge["permission_overwrites"] = [{
                    "id": everyone, "type": 0,
                    "allow": str(VIEW_CHANNEL),
                    "deny": str(SEND_MESSAGES),
                }]
            if type_effectif == FORUM:
                balises = BALISES_BUGS if nom == "bug-reports" else BALISES_IDEES
                charge["available_tags"] = [{"name": b, "moderated": False}
                                            for b in balises]
            salon = appel("POST", "/guilds/%s/channels" % guilde, jeton, charge)
            par_nom[nom] = salon
            time.sleep(0.4)

    # --- mode Communaute ------------------------------------------------
    # Discord n'accepte COMMUNITY que si QUATRE conditions sont reunies dans
    # le meme appel : un salon de regles, un salon d'avis de moderation, une
    # verification a LOW minimum, et le filtre de contenu sur tous les
    # membres. On les fournit d'un bloc : envoyees separement, l'API refuse
    # sans dire laquelle manque.
    #
    # C'est un reglage de TON serveur, donc en clair : ca met la verification
    # sur "email verifie" et le filtre d'images sur "tous les membres". Ce
    # sont les minimums exiges par Discord, pas un choix de ma part.
    if appliquer and not communaute:
        regles = par_nom.get("welcome")
        avis = par_nom.get("server-updates")
        if regles and avis:
            print("\nmode Communaute : activation")
            print("  regles             -> #welcome")
            print("  avis de moderation -> #server-updates (prive)")
            print("  verification       -> email verifie")
            print("  filtre d'images    -> tous les membres")
            appel("PATCH", "/guilds/%s" % guilde, jeton, {
                "features": sorted(set(infos.get("features") or []) |
                                   {"COMMUNITY"}),
                "rules_channel_id": regles["id"],
                "public_updates_channel_id": avis["id"],
                "verification_level": 1,
                "explicit_content_filter": 2,
            })
            communaute = True
            print("  active.")
            # Les salons declares ANNONCE, crees en texte faute de mode
            # Communaute, deviennent de vrais salons d'annonces : les autres
            # serveurs peuvent s'y abonner et republier tes sorties chez eux.
            for _categorie, salons in PLAN:
                for nom, type_salon, _sujet, _diff, _prive in salons:
                    salon = par_nom.get(nom)
                    if (type_salon == ANNONCE and salon
                            and salon.get("type") != ANNONCE):
                        appel("PATCH", "/channels/%s" % salon["id"], jeton,
                              {"type": ANNONCE})
                        salon["type"] = ANNONCE
                        print("  #%-16s converti en salon d'annonces" % nom)
                        time.sleep(0.3)
        else:
            print("\nmode Communaute : NON active, il manque #welcome ou "
                  "#server-updates")

    # --- AutoMod ----------------------------------------------------------
    # Les alertes vont dans le salon STAFF : une alerte de moderation affichee
    # en public apprend surtout aux curieux quels mots declenchent quoi.
    alerte = par_nom.get("server-updates")
    regles_existantes = {
        r["name"] for r in
        (appel("GET", "/guilds/%s/auto-moderation/rules" % guilde, jeton) or [])
    }
    for nom, declencheur, metadonnees, alerter, explication in AUTOMOD:
        if nom in regles_existantes:
            print("automod   %-28s deja presente" % nom)
            continue
        print("automod   %-28s A CREER  (%s)" % (nom, explication))
        if not appliquer:
            continue
        # Le message de refus est limite a 150 caracteres par l'API, et il
        # est lu par un acheteur : il doit dire quoi faire, pas juste "non".
        actions = [{"type": 1, "metadata": {"custom_message":
                    "Blocked by the server rules. If this was a genuine "
                    "support question, post it again without links."}}]
        if alerter and alerte:
            actions.append({"type": 2,
                            "metadata": {"channel_id": alerte["id"]}})
        charge = {"name": nom, "event_type": 1, "trigger_type": declencheur,
                  "enabled": True, "actions": actions}
        if metadonnees:
            charge["trigger_metadata"] = dict(metadonnees)
        appel("POST", "/guilds/%s/auto-moderation/rules" % guilde, jeton,
              charge)
        time.sleep(0.3)

    # --- message d'accueil ------------------------------------------------
    accueil = par_nom.get("welcome")
    if accueil and appliquer:
        deja = appel("GET", "/channels/%s/messages?limit=10" % accueil["id"],
                     jeton)
        if any("Welcome to Nythrox" in (m.get("content") or "") for m in deja):
            print("\naccueil   deja publie")
        else:
            appel("POST", "/channels/%s/messages" % accueil["id"], jeton,
                  {"content": ACCUEIL})
            print("\naccueil   publie dans #welcome")
    elif accueil:
        print("\naccueil   A PUBLIER dans #welcome")

    print("\nTermine." if appliquer else "\nPlan affiche, rien n'a ete ecrit.")
    print("Ensuite, a la main : genere une invitation PERMANENTE "
          "(Expire: Jamais, Utilisations: illimitees) et colle-la dans "
          "src/site.ts, champ support.discordInvite.")


main(sys.argv[1:])
