# -*- coding: utf-8 -*-
"""Annonce dans Discord les produits ajoutes depuis le commit precedent.

Pourquoi le site et pas Fab
---------------------------
La source de verite est `src/content/assets/*.md`, dans TON depot. Tu la
controles, elle est versionnee, et elle contient deja tout ce qu'une annonce
demande : titre, accroche, categorie, prix, lien Fab. Une eventuelle API
vendeur Fab dependrait d'un tiers et n'a pas ete verifiee.

Ce que fait ce script
---------------------
Il compare la liste des produits entre deux commits, et publie un message
Discord par produit AJOUTE. Il ne dit rien sur les modifications, pour ne pas
spammer le salon a chaque correction de faute de frappe.

Il ecrit aussi `public/products.json`, la liste a plat des produits, qui sert
au bot de tickets pour tenir ses causes a jour sans intervention.

Utilisation locale, pour verifier avant de brancher l'automatisation :

    python scripts/annoncer_nouveaux_produits.py --depuis HEAD~1
    python scripts/annoncer_nouveaux_produits.py --depuis HEAD~1 --envoyer

Le webhook n'est jamais ecrit dans un fichier : il vient de la variable
d'environnement DISCORD_WEBHOOK_URL.
"""
import argparse
import json
import os
import pathlib
import re
import subprocess
import sys
import urllib.error
import urllib.request

RACINE = pathlib.Path(__file__).resolve().parents[1]
ASSETS = "src/content/assets"
SORTIE_LISTE = RACINE / "public" / "products.json"

# Couleur de la barre laterale des messages Discord, cobalt de la marque.
COULEUR = 0x3B82F6


def git(*args):
    resultat = subprocess.run(
        ["git", *args], cwd=RACINE, capture_output=True, text=True,
        encoding="utf-8", errors="replace")
    if resultat.returncode != 0:
        raise SystemExit("git %s a echoue :\n%s" % (" ".join(args),
                                                    resultat.stderr.strip()))
    return resultat.stdout


def lire_frontmatter(texte):
    """Frontmatter YAML minimal : juste ce dont l'annonce a besoin.

    On evite volontairement une dependance YAML : le script doit tourner dans
    une action GitHub sans installation, et on ne lit que des champs simples.
    """
    bloc = re.match(r"^---\s*\n(.*?)\n---\s*\n", texte, re.DOTALL)
    if not bloc:
        return {}
    champs = {}
    for ligne in bloc.group(1).splitlines():
        trouve = re.match(r"^([a-zA-Z][a-zA-Z0-9_]*):\s*(.*)$", ligne)
        if not trouve:
            continue
        cle, valeur = trouve.group(1), trouve.group(2).strip()
        if valeur.startswith(("'", '"')) and valeur.endswith(("'", '"')):
            valeur = valeur[1:-1]
        champs[cle] = valeur
    return champs


def produits_a(reference):
    """{slug: champs} des produits presents a une reference git donnee."""
    if reference is None:
        fichiers = [str(p.relative_to(RACINE)).replace("\\", "/")
                    for p in (RACINE / ASSETS).glob("*.md")]
        lire = lambda f: (RACINE / f).read_text(encoding="utf-8")
    else:
        sortie = git("ls-tree", "-r", "--name-only", reference, ASSETS)
        fichiers = [l for l in sortie.splitlines() if l.endswith(".md")]
        lire = lambda f: git("show", "%s:%s" % (reference, f))

    produits = {}
    for fichier in fichiers:
        champs = lire_frontmatter(lire(fichier))
        if not champs.get("title"):
            continue
        if str(champs.get("draft", "")).lower() == "true":
            continue
        slug = pathlib.Path(fichier).stem
        champs["slug"] = slug
        produits[slug] = champs
    return produits


def message(produit, base_url):
    """Un embed Discord par produit. Pas de @everyone : c'est un salon
    d'annonces, les gens s'y abonnent volontairement."""
    lignes = []
    categorie = produit.get("category")
    moteur = produit.get("engine")
    if categorie or moteur:
        lignes.append(" · ".join(x for x in (categorie, moteur) if x))
    prix = produit.get("pricePersonal")
    if prix:
        lignes.append("**%s**" % prix)

    embed = {
        "title": produit["title"],
        "description": produit.get("tagline", ""),
        "color": COULEUR,
        "url": "%s/assets/%s" % (base_url.rstrip("/"), produit["slug"]),
        "footer": {"text": "Nythrox"},
    }
    if lignes:
        embed["fields"] = [{"name": "​", "value": "\n".join(lignes)}]
    if produit.get("fabUrl"):
        embed["fields"] = (embed.get("fields") or []) + [
            {"name": "Fab", "value": produit["fabUrl"]}]
    return {"content": "**New release**", "embeds": [embed]}


def envoyer(charge, webhook):
    donnees = json.dumps(charge).encode("utf-8")
    requete = urllib.request.Request(webhook, data=donnees, method="POST")
    requete.add_header("Content-Type", "application/json")
    requete.add_header("User-Agent", "NythroxReleaseBot/1.0")
    try:
        with urllib.request.urlopen(requete) as reponse:
            return reponse.status
    except urllib.error.HTTPError as erreur:
        raise SystemExit("Discord a refuse l'annonce : %s\n%s"
                         % (erreur.code, erreur.read().decode("utf-8", "replace")))


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--depuis", default="HEAD~1",
                        help="reference git de comparaison")
    parser.add_argument("--envoyer", action="store_true",
                        help="publie reellement ; sans ce drapeau, simule")
    parser.add_argument("--base-url", default="https://nythrox-asset.com")
    args = parser.parse_args(argv)

    avant = produits_a(args.depuis)
    apres = produits_a(None)
    nouveaux = [apres[slug] for slug in apres if slug not in avant]

    # La liste a plat, consommee par le bot de tickets pour ses causes.
    SORTIE_LISTE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE_LISTE.write_text(json.dumps(
        {"produits": [{"slug": p["slug"], "title": p["title"],
                       "category": p.get("category", "")}
                      for p in sorted(apres.values(), key=lambda x: x["title"])]},
        ensure_ascii=False, indent=2), encoding="utf-8")

    print("produits avant %s : %d" % (args.depuis, len(avant)))
    print("produits maintenant  : %d" % len(apres))
    print("nouveaux             : %d" % len(nouveaux))
    print("liste ecrite         : public/products.json")

    if not nouveaux:
        print("\nrien a annoncer.")
        return 0

    webhook = os.environ.get("DISCORD_WEBHOOK_URL", "").strip()
    for produit in nouveaux:
        charge = message(produit, args.base_url)
        print("\n--- %s ---" % produit["title"])
        print(json.dumps(charge, ensure_ascii=False, indent=2)[:600])
        if args.envoyer:
            if not webhook:
                raise SystemExit("DISCORD_WEBHOOK_URL absent, envoi annule")
            envoyer(charge, webhook)
            print("publie.")
    if not args.envoyer:
        print("\nSIMULATION : ajoute --envoyer pour publier reellement.")
    return 0


sys.exit(main())
