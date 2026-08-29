---
title: "Greece Dust 2"
tagline: "A Greek seaside town built as a 5v5 combat map: two bomb sites, tight alleys, a tunnel, a wine cellar and a warehouse."
intro: "A Greek seaside town built as a 5v5 combat map. White houses with blue shutters, cobblestone streets, a stone windmill, a bell tower facing the sea, cafe terraces and a vaulted wine cellar. The map is built around two bomb sites, A and B, connected by tight passages, alleys and a tunnel under the street. Delivered as a complete Unreal Engine 5.8 project, ready to play."

# Passer a false quand la fiche Fab est publiee et fabUrl renseigne.
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

# Demo Windows construite (2,506 Gio) mais PAS ENCORE HEBERGEE : au-dessus du
# plafond de 2 Gio par fichier des releases GitHub. Reactiver ces deux champs
# des que le fichier est heberge (split, autre hote, ou demo allegee).
# demoDownloadUrl: https://github.com/nythrox-asset/nythrox-asset/releases/download/demos-v1/GreeceDust2_Demo_Windows.zip
# demoDownloadNote: Windows · 2.69 GB

features:
  - "Fully built map, open the project and play, nothing to import"
  - "Two bomb sites, A and B, with direction signs, tight passages, alleys and a tunnel under the street"
  - "9,485 unique Static Meshes placed 10,827 times across the map"
  - "1.9 million unique triangles (2.24 million as placed)"
  - "Nanite enabled on the Static Meshes, so no LODs to manage"
  - "Collision on every model (Complex Collision As Simple), 10,827 blocking instances, 0 errors"
  - "Animated sea with real Gerstner waves and real-time reflections"
  - "Dynamic Lumen lighting with ray tracing and Virtual Shadow Maps, nothing baked"
  - "Lightmap UVs verified on every mesh, none missing"

includes: "Complete Unreal Engine 5.8 project (Complete project), plus the Blender source file (.blend)."
notes: "This pack contains environment geometry only, no weapons, no game logic and no bomb/defuse scripts, the bomb sites are set dressing and signage. Doors are static geometry; interactive door functionality requires the separate Nythrox Interactive Door plugin. The windmills are static and do not turn. The animated water uses a Gerstner wave shader derived from the MIT-licensed Fishies project, with its notice included. No Overview map in this release."
idealFor: "Objective-based multiplayer modes, search and destroy prototypes, or as a Greek coastal town environment for any project."

specs:
  formats: [Unreal project, Blender]
  meshes: 9485
  triangles: "1,903,193"
  collision: Complex Collision As Simple on every mesh (10,827 instances, 0 failures)
  lods: None (Nanite)
  animated: "Water surface only (Gerstner wave shader)"
  rigged: false
  characters: 0

i18n:
  fr:
    title: "Greece Dust 2"
    tagline: "Une ville grecque au bord de la mer, conçue comme une carte de combat 5v5 : deux sites de bombe, des ruelles, un tunnel, une cave à vin et un entrepôt."
    intro: "Une ville grecque au bord de la mer, construite comme une carte de combat 5v5. Maisons blanches aux volets bleus, ruelles pavées, moulin en pierre, clocher face à la mer, terrasses de café et cave à vin voûtée. La map est organisée autour de deux sites de bombe, A et B, reliés par des passages étroits, des ruelles et un tunnel sous la rue. Livrée en projet Unreal Engine 5.8 complet, prêt à jouer."
    features:
      - "Map entièrement montée, vous ouvrez le projet et vous jouez, aucun import à faire"
      - "Deux sites de bombe A et B, avec panneaux de direction, passages étroits, ruelles et un tunnel sous la rue"
      - "9 485 modèles 3D différents, placés 10 827 fois dans la map"
      - "1,9 million de triangles uniques (2,24 millions une fois placés)"
      - "Nanite activé sur les modèles, donc aucun LOD à gérer"
      - "Collision sur chaque modèle (Complex Collision As Simple), 10 827 objets bloquants, 0 erreur"
      - "Mer animée avec de vraies vagues de Gerstner et des reflets en temps réel"
      - "Éclairage dynamique Lumen avec ray tracing et Virtual Shadow Maps, rien de précalculé"
      - "UV de lightmap vérifiés sur tous les modèles, aucun manquant"
    includes: "Projet Unreal Engine 5.8 complet (Complete project), plus le fichier source Blender (.blend)."
    notes: "Ce pack contient uniquement la géométrie d'environnement, aucune arme, aucune logique de jeu et aucun script de pose/désamorçage : les sites de bombe sont du décor et de la signalétique. Les portes sont de la géométrie statique ; la fonctionnalité de porte interactive nécessite le plugin Nythrox Interactive Door, vendu séparément. Les moulins sont statiques et ne tournent pas. L'eau animée utilise un shader à vagues de Gerstner dérivé du projet Fishies sous licence MIT, notice incluse. Pas de carte Overview dans cette version."
    idealFor: "Modes multijoueur par objectifs, prototypes de search and destroy, ou comme environnement de ville côtière grecque pour n'importe quel projet."
---
