# -*- coding: utf-8 -*-
"""Ajoute les cles de navigation 'nav.support' et 'nav.docs', EN, ES, FR.

Les cles sont inserees juste apres 'nav.about' de chaque bloc de langue, pour
respecter l'ordre existant. Idempotent : si la cle est deja la, on ne fait rien.
"""
import io
import pathlib

FICHIER = pathlib.Path(__file__).resolve().parents[1] / "src" / "i18n" / "ui.ts"

# Ancre exacte par langue -> lignes a inserer juste apres.
AJOUTS = {
    "    'nav.about': 'About',\n": (
        "    'nav.docs': 'Docs',\n"
        "    'nav.support': 'Support',\n"),
    "    'nav.about': 'Acerca de',\n": (
        "    'nav.docs': 'Documentación',\n"
        "    'nav.support': 'Soporte',\n"),
    "    'nav.about': 'À propos',\n": (
        "    'nav.docs': 'Documentation',\n"
        "    'nav.support': 'Support',\n"),
}

texte = FICHIER.read_text(encoding="utf-8")
if "'nav.support'" in texte:
    print("cles deja presentes, rien a faire")
else:
    for ancre, ajout in AJOUTS.items():
        if ancre not in texte:
            raise SystemExit("ancre introuvable, insertion annulee: %r" % ancre)
        texte = texte.replace(ancre, ancre + ajout, 1)
    FICHIER.write_text(texte, encoding="utf-8")
    print("cles nav.docs et nav.support ajoutees pour EN, ES, FR")
