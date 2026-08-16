/* ------------------------------------------------------------------ *
 *  Réglages globaux du site : édite ICI, ça se propage partout.       *
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

  /* ---------------------------------------------------------------- *
   *  SUPPORT                                                          *
   *  Le lien Discord est le canal de support annonce sur Fab. Tant    *
   *  qu'il est vide, la page support affiche un etat "bientot" au     *
   *  lieu d'un bouton mort : un acheteur qui clique dans le vide est  *
   *  pire que pas de bouton du tout.                                  *
   * ---------------------------------------------------------------- */
  support: {
    /**
     * Identifiant Discord de Nathan, donne a l'acheteur qui veut discuter.
     * Decision du 29/07/2026 : PAS de serveur. Un serveur demande des salons a
     * moderer, un outil de tickets et une presence a tenir ; un identifiant se
     * donne en une ligne. Vide = la page n'affiche rien plutot qu'un contact
     * mort.
     */
    discordHandle: 'nythrox_asset',
    /** Adresse de repli pour ceux qui n'utilisent pas Discord. */
    email: '',
    /** Delai de reponse annonce. Ne promets que ce que tu tiens. */
    responseTime: '48h',
  },

  /* ---------------------------------------------------------------- *
   *  LIENS PRODUIT, repris dans la fiche Fab.                         *
   * ---------------------------------------------------------------- */
  doorSystem: {
    /** Video de presentation (YouTube, Vimeo...). */
    trailerUrl: '',
    /** Page de vente Fab du plugin. */
    fabUrl: '',
  },
} as const;
