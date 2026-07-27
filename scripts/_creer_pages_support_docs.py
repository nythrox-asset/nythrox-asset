# -*- coding: utf-8 -*-
"""Cree les enveloppes de pages support et documentation, EN, FR, ES.

Le site suit un motif net : le composant deduit la langue et chaque page
localisee n'est qu'une enveloppe d'une ligne (voir src/pages/fr/index.astro).
Ce script se contente de poser ces enveloppes, sans dupliquer de contenu.

Idempotent : relancer n'ecrase que ce qu'il a lui-meme genere.
"""
import pathlib

RACINE = pathlib.Path(__file__).resolve().parents[1] / "src" / "pages"

PAGES = {
    # chemin relatif           : (profondeur, composant)
    "support.astro": ("../components/SupportBody.astro", "SupportBody"),
    "fr/support.astro": ("../../components/SupportBody.astro", "SupportBody"),
    "es/support.astro": ("../../components/SupportBody.astro", "SupportBody"),
    "docs/interactive-door-system.astro": (
        "../../components/DocsDoorBody.astro", "DocsDoorBody"),
    "fr/docs/interactive-door-system.astro": (
        "../../../components/DocsDoorBody.astro", "DocsDoorBody"),
    "es/docs/interactive-door-system.astro": (
        "../../../components/DocsDoorBody.astro", "DocsDoorBody"),
}

MODELE = "---\nimport {nom} from '{chemin}';\n---\n\n<{nom} />\n"

for relatif, (chemin, nom) in PAGES.items():
    cible = RACINE / relatif
    cible.parent.mkdir(parents=True, exist_ok=True)
    cible.write_text(MODELE.format(nom=nom, chemin=chemin), encoding="utf-8")
    print("ecrit  %s" % relatif)

print("%d page(s) posee(s)" % len(PAGES))
