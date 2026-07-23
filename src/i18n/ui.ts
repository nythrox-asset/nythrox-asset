/* ------------------------------------------------------------------ *
 *  Traductions de l'interface (EN / ES / FR).                          *
 *  Ajoute une langue : ajoute son code dans `languages` + un bloc dans *
 *  `ui`. Les textes des ASSETS se traduisent dans leur frontmatter.    *
 * ------------------------------------------------------------------ */

export const defaultLang = 'en' as const;

export const languages = [
  { code: 'en', name: 'English', flag: 'en' },
  { code: 'es', name: 'Español', flag: 'es' },
  { code: 'fr', name: 'Français', flag: 'fr' },
] as const;

export type Lang = (typeof languages)[number]['code'];

export const ui = {
  en: {
    'nav.assets': 'Assets',
    'nav.about': 'About',
    'nav.fabStore': 'Fab store',

    'hero.titleLine1': 'Game-ready worlds,',
    'hero.titleLine2': 'built clean.',
    'hero.subtitle':
      'Environments and modular kits for Unreal Engine. Organized files, verified collisions, drag-and-drop. No cleanup required.',
    'hero.browse': 'Browse assets',
    'hero.visitFab': 'Visit Fab store',

    'assets.heading': 'Assets',
    'assets.countOne': '{n} pack available',
    'assets.countMany': '{n} packs available',
    'assets.comingSoon': 'New packs coming soon',
    'assets.emptyTitle': 'No assets published yet',
    'assets.emptyPre': 'Add a file in ',
    'assets.emptyPost': ' and it appears here automatically.',

    'card.details': 'Details',
    'card.viewOnFab': 'View on Fab',
    'badge.playableDemo': 'Playable demo',
    'badge.video': 'Video',
    'badge.demoMap': 'Demo map',

    'detail.allAssets': 'All assets',
    'detail.whatsIncluded': "What's included",
    'detail.gallery': 'Gallery',
    'detail.technicalDetails': 'Technical details',

    'spec.engine': 'Engine',
    'spec.formats': 'Formats',
    'spec.meshes': 'Meshes',
    'spec.triangles': 'Triangles',
    'spec.materials': 'Materials',
    'spec.textures': 'Textures',
    'spec.textureRes': 'Texture resolution',
    'spec.collision': 'Collision',
    'spec.lods': 'LODs',
    'spec.nanite': 'Nanite',
    'spec.rigged': 'Rigged',
    'spec.animated': 'Animated',
    'spec.characters': 'Characters',
    'common.yes': 'Yes',
    'common.no': 'No',

    'buy.personal': 'Personal',
    'buy.professional': 'Professional',
    'buy.getItOnFab': 'Get it on Fab',
    'buy.comingSoonFab': 'Coming soon to Fab',
    'buy.playDemo': 'Play the demo',
    'buy.demoMapIncluded': 'Demo map included',
    'buy.overviewMapIncluded': 'Overview map included',

    'footer.explore': 'Explore',
    'footer.tagline':
      'Clean, organized, game-ready 3D environments and modular kits for Unreal Engine. Drag-and-drop ready, no cleanup required.',
    'footer.rights': '© {year} Nythrox. All rights reserved.',
    'footer.builtFor': 'Built for the Fab marketplace.',

    'notfound.subtitle': 'This page drifted out of the grid.',
    'notfound.back': 'Back home',

    'gallery.open': 'Open image {i} of {n}',
    'gallery.close': 'Close',
    'gallery.prev': 'Previous',
    'gallery.next': 'Next',
    'gallery.dialog': '{title} gallery',
    'video.title': 'Showcase video',
    'video.play': 'Play: {title}',

    'lang.label': 'Language',
    'site.titleSuffix': 'Game-ready Unreal environments',
    'site.metaDescription':
      'Nythrox crafts clean, organized, game-ready 3D environments and modular kits for Unreal Engine. Drag-and-drop ready, no cleanup required.',
    'skip.content': 'Skip to content',
  },

  es: {
    'nav.assets': 'Recursos',
    'nav.about': 'Acerca de',
    'nav.fabStore': 'Tienda Fab',

    'hero.titleLine1': 'Mundos listos para jugar,',
    'hero.titleLine2': 'bien organizados.',
    'hero.subtitle':
      'Entornos y kits modulares para Unreal Engine. Archivos organizados, colisiones verificadas, arrastra y suelta. Sin limpieza.',
    'hero.browse': 'Ver recursos',
    'hero.visitFab': 'Ir a la tienda Fab',

    'assets.heading': 'Recursos',
    'assets.countOne': '{n} pack disponible',
    'assets.countMany': '{n} packs disponibles',
    'assets.comingSoon': 'Próximamente nuevos packs',
    'assets.emptyTitle': 'Aún no hay recursos publicados',
    'assets.emptyPre': 'Añade un archivo en ',
    'assets.emptyPost': ' y aparecerá aquí automáticamente.',

    'card.details': 'Detalles',
    'card.viewOnFab': 'Ver en Fab',
    'badge.playableDemo': 'Demo jugable',
    'badge.video': 'Vídeo',
    'badge.demoMap': 'Mapa demo',

    'detail.allAssets': 'Todos los recursos',
    'detail.whatsIncluded': 'Qué incluye',
    'detail.gallery': 'Galería',
    'detail.technicalDetails': 'Detalles técnicos',

    'spec.engine': 'Motor',
    'spec.formats': 'Formatos',
    'spec.meshes': 'Mallas',
    'spec.triangles': 'Triángulos',
    'spec.materials': 'Materiales',
    'spec.textures': 'Texturas',
    'spec.textureRes': 'Resolución de texturas',
    'spec.collision': 'Colisión',
    'spec.lods': 'LODs',
    'spec.nanite': 'Nanite',
    'spec.rigged': 'Con rig',
    'spec.animated': 'Animado',
    'spec.characters': 'Personajes',
    'common.yes': 'Sí',
    'common.no': 'No',

    'buy.personal': 'Personal',
    'buy.professional': 'Profesional',
    'buy.getItOnFab': 'Cómpralo en Fab',
    'buy.comingSoonFab': 'Pronto en Fab',
    'buy.playDemo': 'Jugar la demo',
    'buy.demoMapIncluded': 'Mapa demo incluido',
    'buy.overviewMapIncluded': 'Mapa overview incluido',

    'footer.explore': 'Explorar',
    'footer.tagline':
      'Entornos 3D y kits modulares limpios, organizados y listos para Unreal Engine. Listos para arrastrar y soltar, sin limpieza.',
    'footer.rights': '© {year} Nythrox. Todos los derechos reservados.',
    'footer.builtFor': 'Hecho para el marketplace Fab.',

    'notfound.subtitle': 'Esta página se salió de la cuadrícula.',
    'notfound.back': 'Volver al inicio',

    'gallery.open': 'Abrir imagen {i} de {n}',
    'gallery.close': 'Cerrar',
    'gallery.prev': 'Anterior',
    'gallery.next': 'Siguiente',
    'gallery.dialog': 'Galería de {title}',
    'video.title': 'Vídeo demostrativo',
    'video.play': 'Reproducir: {title}',

    'lang.label': 'Idioma',
    'site.titleSuffix': 'Entornos Unreal listos para jugar',
    'site.metaDescription':
      'Nythrox crea entornos 3D limpios, organizados y listos para Unreal Engine, listos para arrastrar y soltar, sin limpieza.',
    'skip.content': 'Saltar al contenido',
  },

  fr: {
    'nav.assets': 'Ressources',
    'nav.about': 'À propos',
    'nav.fabStore': 'Boutique Fab',

    'hero.titleLine1': 'Des mondes prêts à jouer,',
    'hero.titleLine2': 'propres et nets.',
    'hero.subtitle':
      'Environnements et kits modulaires pour Unreal Engine. Fichiers organisés, collisions vérifiées, glisser-déposer. Sans nettoyage.',
    'hero.browse': 'Voir les ressources',
    'hero.visitFab': 'Voir la boutique Fab',

    'assets.heading': 'Ressources',
    'assets.countOne': '{n} pack disponible',
    'assets.countMany': '{n} packs disponibles',
    'assets.comingSoon': 'De nouveaux packs bientôt',
    'assets.emptyTitle': 'Aucune ressource publiée pour l’instant',
    'assets.emptyPre': 'Ajoute un fichier dans ',
    'assets.emptyPost': ' et il apparaît ici automatiquement.',

    'card.details': 'Détails',
    'card.viewOnFab': 'Voir sur Fab',
    'badge.playableDemo': 'Démo jouable',
    'badge.video': 'Vidéo',
    'badge.demoMap': 'Map démo',

    'detail.allAssets': 'Toutes les ressources',
    'detail.whatsIncluded': 'Ce qui est inclus',
    'detail.gallery': 'Galerie',
    'detail.technicalDetails': 'Détails techniques',

    'spec.engine': 'Moteur',
    'spec.formats': 'Formats',
    'spec.meshes': 'Meshes',
    'spec.triangles': 'Triangles',
    'spec.materials': 'Matériaux',
    'spec.textures': 'Textures',
    'spec.textureRes': 'Résolution des textures',
    'spec.collision': 'Collision',
    'spec.lods': 'LODs',
    'spec.nanite': 'Nanite',
    'spec.rigged': 'Riggé',
    'spec.animated': 'Animé',
    'spec.characters': 'Personnages',
    'common.yes': 'Oui',
    'common.no': 'Non',

    'buy.personal': 'Personnelle',
    'buy.professional': 'Professionnelle',
    'buy.getItOnFab': 'Obtenir sur Fab',
    'buy.comingSoonFab': 'Bientôt sur Fab',
    'buy.playDemo': 'Lancer la démo',
    'buy.demoMapIncluded': 'Map démo incluse',
    'buy.overviewMapIncluded': 'Map Overview incluse',

    'footer.explore': 'Explorer',
    'footer.tagline':
      'Environnements 3D et kits modulaires propres, organisés et prêts pour Unreal Engine. Glisser-déposer, sans nettoyage.',
    'footer.rights': '© {year} Nythrox. Tous droits réservés.',
    'footer.builtFor': 'Conçu pour la marketplace Fab.',

    'notfound.subtitle': 'Cette page a quitté la grille.',
    'notfound.back': 'Retour à l’accueil',

    'gallery.open': 'Ouvrir l’image {i} sur {n}',
    'gallery.close': 'Fermer',
    'gallery.prev': 'Précédent',
    'gallery.next': 'Suivant',
    'gallery.dialog': 'Galerie {title}',
    'video.title': 'Vidéo de présentation',
    'video.play': 'Lire : {title}',

    'lang.label': 'Langue',
    'site.titleSuffix': 'Environnements Unreal prêts à jouer',
    'site.metaDescription':
      'Nythrox crée des environnements 3D propres, organisés et prêts pour Unreal Engine, glisser-déposer, sans nettoyage.',
    'skip.content': 'Aller au contenu',
  },
} as const;

export type UIKey = keyof (typeof ui)['en'];
