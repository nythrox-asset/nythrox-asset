---
title: "Greek Dust2"
tagline: "A Greek seaside town built as a 5v5 combat map: two bomb sites, tight alleys, a tunnel, a wine cellar and a warehouse."
intro: "A Greek seaside town built as a 5v5 combat map. White houses with blue shutters, cobblestone streets, a stone windmill, a bell tower facing the sea, cafe terraces and a vaulted wine cellar. The map is built around two bomb sites, A and B, connected by tight passages, alleys and a tunnel under the street. Delivered as a complete Unreal Engine 5.8 project, ready to play."

# Publiee sur Fab le 31/08/2026 sous le titre « Greek Dust2 », mise a jour le
# 27/09/2026. Texte et chiffres realignes sur la fiche Fab le 12/10/2026.
draft: false
featured: false
order: 0
date: 2026-08-29

category: Environment
engine: Unreal Engine 5.8
tags: [combat map, multiplayer arena, greek town, city environment, objective map, aegean, bomb site, game ready]

cover: ./media/greece-dust2-cover.jpg
gallery:
  - ./media/greece-dust2-rooftop-panorama-5.jpg
  - ./media/greece-dust2-rooftop-panorama-4.jpg
  - ./media/greece-dust2-rooftop-panorama-3.jpg
  - ./media/greece-dust2-sea-boats.jpg
  - ./media/greece-dust2-rooftop-panorama-2.jpg
  - ./media/greece-dust2-rooftop-panorama-1.jpg
  - ./media/greece-dust2-fresco-yellow-car.jpg
  - ./media/greece-dust2-seaside-tower.jpg
  - ./media/greece-dust2-oracle-bell-tower.jpg
  - ./media/greece-dust2-wine-cellar.jpg
  - ./media/greece-dust2-cellar-entrance.jpg
  - ./media/greece-dust2-courtyard-truck.jpg
  - ./media/greece-dust2-site-signage.jpg
  - ./media/greece-dust2-courtyard-hydrant.jpg
  - ./media/greece-dust2-fresco-balcony.jpg
  - ./media/greece-dust2-kebab-gate.jpg
  - ./media/greece-dust2-main-street.jpg
  - ./media/greece-dust2-scoops-mural.jpg
  - ./media/greece-dust2-plaza-aegean-scoops.jpg
  - ./media/greece-dust2-street-a-site.jpg
  - ./media/greece-dust2-courtyard-chapel.jpg
  - ./media/greece-dust2-arch-a-site.jpg
  - ./media/greece-dust2-loot-table-2.jpg
  - ./media/greece-dust2-loot-table-1.jpg
  - ./media/greece-dust2-warehouse-stage.jpg

# Contenu livre : une seule carte jouable L_Main, pas d'Overview (choix Nathan).
demoMapIncluded: false
overviewMapIncluded: false

fabUrl: https://www.fab.com/listings/ed941ae2-08b5-4dc8-b730-61829ba60255

# Demo Windows en DEUX fichiers : le .ucas seul depasse le plafond de 2 Gio par
# fichier des releases GitHub, donc part1 (donnees) + part2 (executable et
# moteur). Le lien pointe la page de release qui liste les deux.
demoDownloadUrl: https://github.com/nythrox-asset/nythrox-asset/releases/tag/demos-v1
demoDownloadNote: Windows · 2 files to download · 2.07 GB

features:
  - "Fully built map, open the project and play, nothing to import"
  - "Two bomb sites, A and B, with direction signs, tight passages, alleys and a tunnel under the street"
  - "7,249 different 3D models, each one a separate, editable asset"
  - "4.1 million unique triangles, 2,273 materials and 2,924 textures"
  - "Simple collision on every model, plus hidden blocking volumes where needed"
  - "Sea surface with Unreal's water shading and 12 animated effects"
  - "Rotating props animated in the level"
  - "Dynamic Lumen lighting with sky, sun and fog"
  - "Nanite enabled on the models, no LODs to manage"
  - "Playable Windows demo, walk the whole map before buying"

includes: "Complete Unreal Engine 5.8 project (Complete project), plus the Blender source file (.blend) and a GLB scene."
notes: "Environment geometry only, no weapons and no game logic. The bomb sites are set dressing and signage. Doors are static geometry; interactive door functionality requires the separate Nythrox Interactive Door plugin. No Overview map in this release."
idealFor: "Objective-based multiplayer modes, search and destroy prototypes, or as a Greek coastal town environment for any project."

specs:
  formats: [Unreal project, Blender, GLB]
  meshes: 7249
  triangles: "4.1 million"
  materials: 2273
  textures: 2924
  collision: Simple collision on every model, plus hidden blocking volumes
  lods: None (Nanite)
  animated: "Sea surface, 12 effects and rotating props"
  rigged: false
  characters: 0

i18n:
  fr:
    title: "Greek Dust2"
    tagline: "Une ville grecque au bord de la mer, conçue comme une carte de combat 5v5 : deux sites de bombe, des ruelles, un tunnel, une cave à vin et un entrepôt."
    intro: "Une ville grecque au bord de la mer, construite comme une carte de combat 5v5. Maisons blanches aux volets bleus, ruelles pavées, moulin en pierre, clocher face à la mer, terrasses de café et cave à vin voûtée. La map est organisée autour de deux sites de bombe, A et B, reliés par des passages étroits, des ruelles et un tunnel sous la rue. Livrée en projet Unreal Engine 5.8 complet, prêt à jouer."
    features:
      - "Map entièrement montée, vous ouvrez le projet et vous jouez, aucun import à faire"
      - "Deux sites de bombe A et B, avec panneaux de direction, passages étroits, ruelles et un tunnel sous la rue"
      - "7 249 modèles 3D différents, chacun un asset séparé et modifiable"
      - "4,1 millions de triangles uniques, 2 273 matériaux et 2 924 textures"
      - "Collision simple sur chaque modèle, plus des volumes bloquants cachés là où il en faut"
      - "Surface de mer avec le rendu d'eau d'Unreal et 12 effets animés"
      - "Objets tournants animés dans le niveau"
      - "Éclairage dynamique Lumen avec ciel, soleil et brume"
      - "Nanite activé sur les modèles, aucun LOD à gérer"
      - "Démo Windows jouable, parcourez toute la map avant d'acheter"
    includes: "Projet Unreal Engine 5.8 complet (Complete project), plus le fichier source Blender (.blend) et une scène GLB."
    notes: "Géométrie d'environnement seulement, aucune arme et aucune logique de jeu. Les sites de bombe sont du décor et de la signalétique. Les portes sont de la géométrie statique ; la fonctionnalité de porte interactive nécessite le plugin Nythrox Interactive Door, vendu séparément. Pas de carte Overview dans cette version."
    idealFor: "Modes multijoueur par objectifs, prototypes de search and destroy, ou comme environnement de ville côtière grecque pour n'importe quel projet."
---
