---
title: "Underground Metro Station Environment, Modular Subway Level"
tagline: "A tiled underground station drowned in deep red light: platform with train, long tile corridors, waiting areas and Japanese signage."
intro: "A full underground metro station bathed in deep red light. White ceramic tile walls, tactile paving strips, twin handrails and rows of fluorescent tubes run from the platform, where a train sits with its doors closed, down long empty corridors to the waiting areas and their route map posters. One lift interior keeps its neutral white and green marble, the only place the red light does not reach. Japanese station signage throughout. Built for silence and unease rather than jump scares."
featured: true
order: 500
date: 2026-07-27
category: Environment
engine: Unreal Engine 5.8
tags: [metro, subway, underground, station, platform, liminal, horror, red light, japanese, corridors, train, exploration, unreal, game ready]

# Media : la cover est la planche a texte "METRO LEVEL". Le site ne l'utilise
# JAMAIS en banniere (cover a texte), il prend la 1re de gallery : la meme vue
# du quai, sans le titre, juste le logo.
cover: ./media/metro-level-cover.jpg
gallery:
  - ./media/metro-level-platform-train.jpg
  - ./media/metro-level-tunnel.jpg
  - ./media/metro-level-concourse.jpg
  - ./media/metro-level-notice.jpg
  - ./media/metro-level-lift.jpg
  - ./media/metro-level-waiting.jpg
  - ./media/metro-level-seating.jpg

# Contenu livre
demoMapIncluded: false
overviewMapIncluded: false

# Demo jouable servie par la release GitHub demos-v1 : les builds sont trop
# lourds pour Netlify, qui recommande de rester sous 10 Mo par fichier.
demoDownloadUrl: https://github.com/nythrox-asset/nythrox-asset/releases/download/demos-v1/MetroLevel_Demo_Windows.zip
demoDownloadNote: Windows · 409 MB

# Commercial : renseigner fabUrl avec l'URL PUBLIQUE (www.fab.com/listings/<id>),
# pas celle du portail vendeur (www.fab.com/portal/listings/<id>).
fabUrl: https://www.fab.com/listings/e1a16a1d-0bf8-40eb-953b-6adf9a383a7d

features:
  - "Complete station in one piece: platform with a train carriage, long tile corridors, waiting areas with seating, lift, roller shutters and stairwells"
  - "272 different 3D models and 96,667 triangles"
  - "563 movable lights, all casting shadows, Lumen and hardware ray tracing enabled"
  - "80 material instances and 118 textures up to 1024 x 1024"
  - "Custom collision: hidden blocking meshes and simple collision on every mesh"
  - "Nanite enabled on all 272 meshes, no LODs to manage"
  - "Japanese station signage, route map posters and warning panels, readable up close"
  - "Playable Windows demo available on this page, walk the whole station before buying"
  - "Complete Unreal Engine project: open and play immediately, no import steps required"

includes: "Unreal Engine 5.8 project (Complete project), Blender source file (.blend), and GLB."
notes: "This package contains environment geometry only, no characters, creatures, or scripted events are included. The red lighting is part of the scene and can be changed, every light is a movable light you can recolor or disable. Doors and shutters are static geometry only; interactive door functionality requires the separate Nythrox Interactive Door plugin. No animated effects in this release. Requires Unreal Engine 5.8 and a DirectX 12 GPU with Shader Model 6."
idealFor: "Underground horror and liminal space games, chase or escape sequences, walking sims, found footage and short film sets, or as a base for your own subway level."

specs:
  formats: [Unreal project, GLB, Blender]
  meshes: 272
  triangles: "96,667"
  materials: 80
  textures: 118
  textureRes: up to 1024
  collision: Hidden blocking meshes and simple collision on every mesh
  lods: None (Nanite)
  nanite: true
  animated: None
  rigged: false
  characters: 0

i18n:
  fr:
    title: "Metro Level : station souterraine, quai et couloirs"
    tagline: "Une station souterraine carrelée noyée de lumière rouge : quai avec rame, longs couloirs, salles d'attente et signalétique japonaise."
    intro: "Une station de métro souterraine complète, baignée d'une lumière rouge profonde. Murs de carrelage blanc, bandes podotactiles, doubles mains courantes et rangées de néons courent depuis le quai, où une rame attend portes fermées, jusqu'aux longs couloirs vides puis aux salles d'attente et leurs plans de réseau. Un intérieur d'ascenseur garde son marbre blanc et vert, le seul endroit que le rouge n'atteint pas. Signalétique japonaise partout. Pensée pour le silence et le malaise, pas pour les jump scares."
    features:
      - "Station complète d'un seul tenant : quai avec rame, longs couloirs carrelés, salles d'attente et sièges, ascenseur, rideaux métalliques et cages d'escalier"
      - "272 modèles 3D différents et 96 667 triangles"
      - "563 lumières mobiles, qui projettent toutes des ombres, Lumen et ray tracing matériel activés"
      - "80 instances de matériau et 118 textures jusqu'à 1024 x 1024"
      - "Collision sur mesure : maillages bloquants cachés et collision simple sur chaque mesh"
      - "Nanite activé sur les 272 meshes, aucun LOD à gérer"
      - "Signalétique de station japonaise, plans de réseau et panneaux d'avertissement, lisibles de près"
      - "Démo Windows jouable disponible sur cette page, parcourez toute la station avant d'acheter"
      - "Projet Unreal Engine complet : à ouvrir et jouer immédiatement, sans étape d'import"
    includes: "Projet Unreal Engine 5.8 (Complete project), fichier source Blender (.blend) et GLB."
    notes: "Ce pack contient uniquement la géométrie d'environnement, aucun personnage, créature ou événement scripté n'est inclus. L'éclairage rouge fait partie de la scène et reste modifiable, chaque lumière est mobile, donc recolorable ou désactivable. Portes et rideaux sont de la géométrie statique ; la fonctionnalité de porte interactive nécessite le plugin Nythrox Interactive Door, vendu séparément. Aucun effet animé dans cette version. Demande Unreal Engine 5.8 et une carte graphique DirectX 12 avec Shader Model 6."
    idealFor: "Jeux d'horreur souterrains et espaces liminaux, séquences de poursuite ou d'évasion, walking sims, décors de found footage ou de court métrage, ou base pour votre propre niveau de métro."
  es:
    title: "Metro Level: estación subterránea, andén y pasillos"
    tagline: "Una estación subterránea alicatada inundada de luz roja: andén con tren, largos pasillos, salas de espera y señalética japonesa."
    intro: "Una estación de metro subterránea completa, bañada en una luz roja profunda. Paredes de azulejo blanco, franjas podotáctiles, dobles pasamanos e hileras de fluorescentes recorren desde el andén, donde un tren espera con las puertas cerradas, hasta los largos pasillos vacíos y luego las salas de espera con sus planos de red. El interior de un ascensor conserva su mármol blanco y verde, el único lugar al que el rojo no llega. Señalética japonesa por todas partes. Pensada para el silencio y la inquietud, no para los sustos repentinos."
    features:
      - "Estación completa de una pieza: andén con tren, largos pasillos alicatados, salas de espera con asientos, ascensor, cierres metálicos y huecos de escalera"
      - "272 modelos 3D diferentes y 96.667 triángulos"
      - "563 luces móviles, todas proyectan sombras, Lumen y ray tracing por hardware activados"
      - "80 instancias de material y 118 texturas de hasta 1024 x 1024"
      - "Colisión a medida: mallas de bloqueo ocultas y colisión simple en cada malla"
      - "Nanite activado en las 272 mallas, sin LOD que gestionar"
      - "Señalética de estación japonesa, planos de red y paneles de advertencia, legibles de cerca"
      - "Demo jugable de Windows disponible en esta página, recorre toda la estación antes de comprar"
      - "Proyecto Unreal Engine completo: ábrelo y juega de inmediato, sin pasos de importación"
    includes: "Proyecto Unreal Engine 5.8 (Complete project), archivo fuente Blender (.blend) y GLB."
    notes: "Este pack contiene únicamente la geometría del entorno, no incluye personajes, criaturas ni eventos con scripts. La iluminación roja forma parte de la escena y se puede cambiar, todas las luces son móviles y se pueden recolorear o desactivar. Las puertas y los cierres son geometría estática; la funcionalidad de puerta interactiva requiere el plugin Nythrox Interactive Door, vendido por separado. Sin efectos animados en esta versión. Requiere Unreal Engine 5.8 y una GPU DirectX 12 con Shader Model 6."
    idealFor: "Juegos de terror subterráneo y espacios liminales, secuencias de persecución o huida, walking sims, decorados de found footage o cortometraje, o como base para tu propio nivel de metro."
---
