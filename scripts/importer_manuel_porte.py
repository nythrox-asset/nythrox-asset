# -*- coding: utf-8 -*-
"""Importe le manuel du Door System depuis son README vers le site.

Une seule source de verite : le README livre AVEC le plugin. Ce script le
decoupe en deux fichiers markdown, anglais et francais, que la page de
documentation rend telle quelle. Quand tu publies une nouvelle version du
plugin, relance ce script et le site suit.

    python scripts/importer_manuel_porte.py <chemin du README.md>

Sans argument, il cherche le README du template du depot export_map_ROBLOX.
"""
import io
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parents[1]
SORTIE = RACINE / "src" / "content" / "docs"

DEFAUTS = [
    pathlib.Path(
        r"C:\Users\natha\Desktop\export_map_ROBLOX\blender script"
        r"\unreal_templates\NythroxDoorSystem\README.md"),
    pathlib.Path(r"C:\Users\natha\AppData\Local\Temp\README.md"),
]

# Titres qui ouvrent chaque manuel dans le README.
ANCRE_EN = re.compile(r"^##\s+English manual\s*$", re.MULTILINE)
ANCRE_FR = re.compile(r"^##\s+Manuel fran\u00e7ais\s*$", re.MULTILINE)


def trouver_source(argv):
    if len(argv) > 1:
        chemin = pathlib.Path(argv[1])
        if not chemin.is_file():
            raise SystemExit("README introuvable : %s" % chemin)
        return chemin
    for candidat in DEFAUTS:
        if candidat.is_file():
            return candidat
    raise SystemExit(
        "aucun README trouve. Passe son chemin en argument.\n"
        "Cherches : %s" % "\n           ".join(str(c) for c in DEFAUTS))


def decouper(texte):
    """Rend (corps anglais, corps francais), sans les titres de section."""
    depart_en = ANCRE_EN.search(texte)
    depart_fr = ANCRE_FR.search(texte)
    if not depart_en or not depart_fr:
        raise SystemExit(
            "les deux manuels n'ont pas ete reperes ; le README a-t-il change "
            "de structure ?")
    corps_en = texte[depart_en.end():depart_fr.start()]
    corps_fr = texte[depart_fr.end():]
    # La ligne de separation qui precede le manuel francais n'a plus de sens
    # une fois les deux manuels separes.
    corps_en = re.sub(r"\n-{3,}\s*\n\s*$", "\n", corps_en)
    # Les titres passent d'un cran : ### devient ## dans une page dediee.
    monter = lambda bloc: re.sub(r"^(#{3,})\s", lambda m: "#" * (len(m.group(1)) - 1) + " ",
                                 bloc, flags=re.MULTILINE)
    return monter(corps_en).strip() + "\n", monter(corps_fr).strip() + "\n"


def main(argv):
    source = trouver_source(argv)
    texte = io.open(source, encoding="utf-8").read()
    version = ""
    premier = re.search(r"^#\s+(.+)$", texte, re.MULTILINE)
    if premier:
        version = premier.group(1).strip()

    corps_en, corps_fr = decouper(texte)
    SORTIE.mkdir(parents=True, exist_ok=True)

    entete = (
        "---\n"
        "title: Interactive Door System\n"
        "source: %s\n"
        "version: %s\n"
        "---\n\n"
    )
    (SORTIE / "door-system-en.md").write_text(
        entete % (source.name, version) + corps_en, encoding="utf-8")
    (SORTIE / "door-system-fr.md").write_text(
        entete % (source.name, version) + corps_fr, encoding="utf-8")

    print("source  : %s" % source)
    print("version : %s" % (version or "inconnue"))
    print("ecrit   : src/content/docs/door-system-en.md (%d lignes)"
          % corps_en.count("\n"))
    print("ecrit   : src/content/docs/door-system-fr.md (%d lignes)"
          % corps_fr.count("\n"))


main(sys.argv)
