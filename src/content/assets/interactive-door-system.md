---
title: Nythrox Interactive Door System
tagline: "Turn any imported mesh into a working interactive door in under a minute, even when its pivot is broken."
intro: "Nythrox Interactive Door System builds a virtual hinge from the door's real geometry, so meshes coming from CAD, scans, kitbashes or game exports open cleanly without a round-trip through Blender. Guided editor panel, in-editor preview before Play mode, locking, sounds, Blueprint events and replicated door state. A focused tool for doors, not a generic interaction framework."
# Masque du site (decision Nathan 27/07/2026) : la fiche existe toujours et
# reste modifiable, elle n'apparait simplement plus dans la boutique ni dans
# les listes. Repasser a false le jour ou le plugin est publie sur Fab.
draft: true
featured: false
order: 300
date: 2026-07-27
category: Plugin
engine: Unreal Engine 5.8
tags: [plugin, door, interactive, hinge, pivot, unreal engine, ue5, blueprint, tool, editor tool, multiplayer, c++]

# Media : aucune capture pour l'instant, le site affiche le visuel de marque.
# Ajoute une cover et une galerie ici quand les captures sont pretes.
# cover: ./media/door-system-cover.jpg
# gallery:
#   - ./media/door-system-panel.jpg

# Commercial : renseigne fabUrl des que la fiche Fab est publiee.
# fabUrl: https://www.fab.com/listings/...

features:
  - "Guided editor panel: select the meshes, record closed, record open, save"
  - Detect frame measures the real jamb of the opening and calibrates the hinge inset in one click
  - Preview the full animation in the editor, without entering Play mode
  - Virtual hinge on the detected slab edge, refined by hinge inset and a leaf-face pivot for thick slabs
  - "Demonstrated mode: the door rotates around the exact centre of the pose you recorded, ideal for unusual frames"
  - Sliding doors supported by the same workflow, no hinge settings needed
  - Locking, auto-close delay, open/close/locked sounds, motion easing
  - "Blueprint events: On Door Opened, On Door Closed, On Interaction Denied"
  - Linked doors for double leaves and airlocks
  - Localized interaction prompt in English, French, German and Spanish
  - Replicated door state for networked games, server authoritative

includes: "Unreal Engine 5.8 plugin for Windows 64-bit, Editor and Runtime modules, complete C++ source, and a full manual in English and French."
notes: "Doors only. This is a focused tool, not a generic interaction framework. The demo scenes shown in the gallery are not included. A level-placed door has no owning connection, so a remote client must route its interaction through an actor it owns, which is one Blueprint node and documented in the manual."
idealFor: "Any project importing door meshes from CAD, photogrammetry, kitbashes or other engines, archviz walkthroughs, horror and exploration games, and level designers who need doors working now rather than after a Blender round-trip."

specs:
  formats: [Unreal plugin]
  engineVersion: "5.8 (tested)"
  platforms: Win64
  source: Complete C++ included
  modules: "NythroxDoorSystem (Runtime), NythroxDoorSystemEditor (Editor)"
  network: Replicated door state, server authoritative
  documentation: English and French manual included
  automationTests: true

i18n:
  fr:
    title: Nythrox Interactive Door System
    tagline: "Transforme n'importe quel mesh importé en porte interactive fonctionnelle en moins d'une minute, même quand son pivot est cassé."
    intro: "Nythrox Interactive Door System construit une charnière virtuelle à partir de la géométrie réelle de la porte. Les meshes venant de CAO, de scans, de kitbash ou d'exports de jeu s'ouvrent proprement, sans détour par Blender. Panneau guidé dans l'éditeur, aperçu avant le mode Jeu, verrouillage, sons, événements Blueprint et état de porte répliqué. Un outil ciblé sur les portes, pas un cadre d'interaction générique."
    features:
      - "Panneau guidé : sélectionne les meshes, enregistre la position fermée, la position ouverte, sauvegarde"
      - Détecter le cadre mesure le dormant réel de l'ouverture et calibre le retrait de charnière en un clic
      - Prévisualise l'animation complète dans l'éditeur, sans passer en mode Jeu
      - Charnière virtuelle sur l'arête de vantail détectée, affinée par le retrait de charnière et un pivot en face de vantail
      - "Mode Demonstrated : la porte tourne autour du centre exact de la pose enregistrée, idéal pour les encadrements inhabituels"
      - Portes coulissantes prises en charge par la même procédure, sans réglage de charnière
      - Verrouillage, fermeture automatique, sons d'ouverture, de fermeture et de refus, lissage du mouvement
      - "Événements Blueprint : On Door Opened, On Door Closed, On Interaction Denied"
      - Portes liées, pour les doubles vantaux et les sas
      - Invite d'interaction localisée en anglais, français, allemand et espagnol
      - État de porte répliqué pour les jeux en réseau, autorité serveur
    includes: "Plugin Unreal Engine 5.8 pour Windows 64 bits, modules Editor et Runtime, source C++ complète, et un manuel complet en anglais et en français."
    notes: "Uniquement des portes. C'est un outil ciblé, pas un cadre d'interaction générique. Les scènes de démonstration de la galerie ne sont pas incluses. Une porte posée dans le niveau n'a pas de connexion propriétaire : un client distant doit router son interaction par un acteur qu'il possède, ce qui tient en un nœud Blueprint et qui est documenté dans le manuel."
    idealFor: "Tout projet important des portes venant de CAO, de photogrammétrie, de kitbash ou d'un autre moteur, les visites d'architecture, les jeux d'horreur et d'exploration, et les level designers qui veulent des portes qui marchent maintenant plutôt qu'après un aller-retour par Blender."
  es:
    title: Nythrox Interactive Door System
    tagline: "Convierte cualquier mesh importado en una puerta interactiva funcional en menos de un minuto, incluso con el pivote roto."
    intro: "Nythrox Interactive Door System construye una bisagra virtual a partir de la geometría real de la puerta. Los meshes de CAD, escaneos, kitbash o exportaciones de otros motores se abren limpiamente, sin pasar por Blender. Panel guiado en el editor, previsualización antes del modo Juego, bloqueo, sonidos, eventos Blueprint y estado de puerta replicado."
    includes: "Plugin de Unreal Engine 5.8 para Windows 64 bits, módulos Editor y Runtime, código fuente C++ completo y manual en inglés y francés."
    notes: "Solo puertas. Es una herramienta enfocada, no un framework de interacción genérico. Las escenas de demostración de la galería no están incluidas."
---
