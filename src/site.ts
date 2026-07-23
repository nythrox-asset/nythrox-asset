/* ------------------------------------------------------------------ *
 *  Réglages globaux du site — édite ICI, ça se propage partout.       *
 * ------------------------------------------------------------------ */
export const SITE = {
  name: 'Nythrox',
  /** Accroche affichée sous le logo sur l'accueil. */
  tagline: 'Game-ready environments & modular kits for Unreal Engine.',
  /** Description SEO par défaut (balise <meta description>). */
  description:
    'Nythrox crafts clean, organized, game-ready 3D environments and modular kits for Unreal Engine. Drag-and-drop ready, no cleanup required.',
  /** URL de production (aussi dans astro.config.mjs). */
  url: 'https://nythrox-asset.com',

  /** Ta boutique / profil vendeur Fab.  ⚠️ Remplace par ta vraie URL. */
  fabStoreUrl: 'https://www.fab.com/sellers/Nythrox',

  /** Liens sociaux (laisse vide '' pour masquer). */
  social: {
    youtube: '',
    x: '',
    discord: '',
    email: '',
  },
} as const;
