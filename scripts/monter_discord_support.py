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
Categories, salons (dont deux forums), roles, permissions de diffusion,
balises de forum, et le message d'accueil. Idempotent : il compare par NOM et
ne recree jamais ce qui existe deja, donc tu peux le relancer sans crainte.

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
PLAN = [
    ("INFORMATION", [
        ("welcome", ANNONCE, "Rules and how to ask for help", True),
        ("announcements", ANNONCE, "Releases and important news", True),
        ("changelog", ANNONCE, "One entry per published version", True),
    ]),
    ("SUPPORT", [
        ("support-en", TEXTE, "Support in English", False),
        ("support-fr", TEXTE, "Support en francais", False),
        ("bug-reports", FORUM, "One thread per bug", False),
        ("feature-requests", FORUM, "One thread per idea", False),
    ]),
    ("COMMUNITY", [
        ("showcase", TEXTE, "What you built with Nythrox packs", False),
        ("general", TEXTE, "Anything else", False),
    ]),
]

# Balises du forum des bugs. Un forum sans balises redevient un salon en vrac.
BALISES_BUGS = ["Door System", "Selection & Assembly", "Asset pack",
                "Confirmed", "Fixed", "Not reproducible"]
BALISES_IDEES = ["Door System", "Selection & Assembly", "Asset pack",
                 "Planned", "Declined"]

ROLES = [
    # (nom, couleur, mentionnable)
    ("Verified buyer", 0x3B82F6, False),
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
    print("serveur : %s\n" % infos.get("name"))

    existants = appel("GET", "/guilds/%s/channels" % guilde, jeton)
    par_nom = {c["name"]: c for c in existants}
    roles_existants = {r["name"]: r
                       for r in appel("GET", "/guilds/%s/roles" % guilde, jeton)}
    everyone = roles_existants.get("@everyone", {}).get("id", guilde)

    # --- roles ---------------------------------------------------------
    for nom, couleur, mentionnable in ROLES:
        if nom in roles_existants:
            print("role      %-22s deja present" % nom)
            continue
        print("role      %-22s A CREER" % nom)
        if appliquer:
            appel("POST", "/guilds/%s/roles" % guilde, jeton,
                  {"name": nom, "color": couleur,
                   "mentionable": mentionnable, "hoist": True})

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

        for nom, type_salon, sujet, diffusion in salons:
            if nom in par_nom:
                print("  salon   %-22s deja present" % nom)
                continue
            etiquette = {ANNONCE: "annonce", FORUM: "forum",
                         TEXTE: "texte"}[type_salon]
            print("  salon   %-22s A CREER (%s)" % (nom, etiquette))
            if not appliquer:
                continue
            charge = {"name": nom, "type": type_salon, "topic": sujet}
            if parent:
                charge["parent_id"] = parent["id"]
            if diffusion:
                # Salon de diffusion : @everyone lit mais n'ecrit pas.
                charge["permission_overwrites"] = [{
                    "id": everyone, "type": 0,
                    "allow": str(VIEW_CHANNEL),
                    "deny": str(SEND_MESSAGES),
                }]
            if type_salon == FORUM:
                balises = BALISES_BUGS if nom == "bug-reports" else BALISES_IDEES
                charge["available_tags"] = [{"name": b, "moderated": False}
                                            for b in balises]
            salon = appel("POST", "/guilds/%s/channels" % guilde, jeton, charge)
            par_nom[nom] = salon
            time.sleep(0.4)

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
