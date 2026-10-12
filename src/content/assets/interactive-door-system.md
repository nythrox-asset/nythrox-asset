---
title: Nythrox Interactive Door System
tagline: "Works with any door: turn any imported door mesh into a working interactive door in a few clicks, even when its pivot is in the wrong place."
intro: "Works with any door. Nythrox Interactive Door System turns any imported door mesh into a working interactive door in a few clicks, even when its pivot is in the wrong place. It builds a virtual hinge from the door's real geometry, so the leaf swings on its real edge and stays against its frame, with no trip back to your 3D software."

# Publie sur Fab le 30/09/2026. Description reprise mot pour mot de la fiche
# Fab le 12/10/2026 (What it does, What's included, Technical details, Notes).
draft: false
featured: false
order: 300
date: 2026-07-27
category: Plugin
engine: Unreal Engine 5.8
tags: [plugin, door, interactive, hinge, pivot, unreal engine, ue5, blueprint, tool, editor tool, multiplayer, c++]

# Images : celles de la fiche Fab, dans le meme ordre (relevees le 12/10/2026).
cover: ./media/interactive-door-system-fab-01.jpg
gallery:
  - ./media/interactive-door-system-fab-01.jpg
  - ./media/interactive-door-system-fab-02.jpg
  - ./media/interactive-door-system-fab-03.jpg
  - ./media/interactive-door-system-fab-04.jpg
  - ./media/interactive-door-system-fab-05.jpg
  - ./media/interactive-door-system-fab-06.jpg

fabUrl: https://www.fab.com/listings/f6179ac0-8dfc-4ca2-9bdc-395ee75713f4

featuresTitle: "What it does"
features:
  - "Guided panel: create the door, rotate it open, record, done."
  - "Virtual hinge on the real leaf edge and face, handles and knobs ignored."
  - "Detect frame calibrates the hinge on the jamb of the opening."
  - "Editor preview plays the motion without entering Play mode."
  - "Swing and sliding doors, linked double doors and interlocked airlocks."
  - "Focused door: one key press opens only the door the player looks at."
  - "Multiplayer ready: server-authoritative, clients open doors with no setup."
  - "Gameplay options: lock, auto-close, sounds, easing and Blueprint events."

included:
  - "Full C++ source, Runtime and Editor modules"
  - "Demo level with five door setups and seven door Blueprints"
  - "Illustrated PDF manual and README, in English"
  - "Panel, dialogs and in-game prompt in 4 languages: English, French, German, Spanish"
  - "11 automated tests, including two-player network tests"

noteList:
  - "Unreal Engine 5.8, Windows 64-bit only."
  - "Doors only: a focused tool, not a generic interaction framework. Environments shown in the gallery are not included."

specs:
  formats: [Unreal plugin]
  engineVersion: "5.8"
  platforms: "Windows (development), Win64 (target builds)"
  source: Complete C++ included
  modules: "NythroxDoorSystem (Runtime), NythroxDoorSystemEditor (Editor)"
  network: "Replicated, server-authoritative"
  documentation: Illustrated PDF manual and README in English
  automationTests: true

i18n:
  fr:
    title: Nythrox Interactive Door System
    tagline: "Marche avec n'importe quelle porte : transforme n'importe quel mesh de porte importé en porte interactive en quelques clics, même quand son pivot est mal placé."
    intro: "Marche avec n'importe quelle porte. Nythrox Interactive Door System transforme n'importe quel mesh de porte importé en porte interactive fonctionnelle en quelques clics, même quand son pivot est mal placé. Il construit une charnière virtuelle à partir de la géométrie réelle de la porte : le vantail tourne sur sa vraie arête et reste contre son cadre, sans retour dans votre logiciel 3D."
    featuresTitle: "Ce qu'il fait"
    features:
      - "Panneau guidé : créez la porte, tournez-la en position ouverte, enregistrez, c'est fait."
      - "Charnière virtuelle sur la vraie arête et la vraie face du vantail, poignées et boutons ignorés."
      - "Détecter le cadre cale la charnière sur le montant de l'ouverture."
      - "L'aperçu dans l'éditeur joue le mouvement sans passer en mode Jeu."
      - "Portes battantes et coulissantes, doubles portes liées et sas verrouillés entre eux."
      - "Porte visée : une touche ouvre seulement la porte que le joueur regarde."
      - "Prêt pour le multijoueur : autorité serveur, les clients ouvrent les portes sans réglage."
      - "Options de jeu : verrou, fermeture automatique, sons, lissage et événements Blueprint."
    included:
      - "Source C++ complète, modules Runtime et Editor"
      - "Niveau de démonstration avec cinq montages de portes et sept Blueprints de porte"
      - "Manuel PDF illustré et README, en anglais"
      - "Panneau, dialogues et invite en jeu en 4 langues : anglais, français, allemand, espagnol"
      - "11 tests automatisés, dont des tests réseau à deux joueurs"
    noteList:
      - "Unreal Engine 5.8, Windows 64 bits seulement."
      - "Uniquement des portes : un outil ciblé, pas un cadre d'interaction générique. Les environnements montrés dans la galerie ne sont pas inclus."
  es:
    title: Nythrox Interactive Door System
    tagline: "Funciona con cualquier puerta: convierte cualquier malla de puerta importada en una puerta interactiva en unos clics, incluso con el pivote mal colocado."
    intro: "Funciona con cualquier puerta. Nythrox Interactive Door System convierte cualquier malla de puerta importada en una puerta interactiva funcional en unos clics, incluso cuando su pivote está mal colocado. Construye una bisagra virtual a partir de la geometría real de la puerta: la hoja gira sobre su borde real y permanece contra su marco, sin volver a tu software 3D."
    featuresTitle: "Qué hace"
    features:
      - "Panel guiado: crea la puerta, gírala hasta abrirla, graba y listo."
      - "Bisagra virtual en el borde y la cara reales de la hoja, ignorando manillas y pomos."
      - "Detectar marco calibra la bisagra sobre la jamba del hueco."
      - "La vista previa del editor reproduce el movimiento sin entrar en modo Juego."
      - "Puertas batientes y correderas, puertas dobles enlazadas y esclusas enclavadas."
      - "Puerta enfocada: una tecla abre solo la puerta que mira el jugador."
      - "Listo para multijugador: autoridad del servidor, los clientes abren puertas sin configuración."
      - "Opciones de juego: bloqueo, cierre automático, sonidos, suavizado y eventos Blueprint."
    included:
      - "Código fuente C++ completo, módulos Runtime y Editor"
      - "Nivel de demostración con cinco montajes de puertas y siete Blueprints de puerta"
      - "Manual PDF ilustrado y README, en inglés"
      - "Panel, diálogos e indicación en juego en 4 idiomas: inglés, francés, alemán, español"
      - "11 pruebas automatizadas, incluidas pruebas de red con dos jugadores"
    noteList:
      - "Unreal Engine 5.8, solo Windows 64 bits."
      - "Solo puertas: una herramienta enfocada, no un framework de interacción genérico. Los entornos mostrados en la galería no están incluidos."
---
