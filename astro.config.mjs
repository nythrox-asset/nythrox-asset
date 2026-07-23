// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

// Domaine de production. Change-le si tu déploies ailleurs.
const SITE = 'https://nythrox-asset.com';

// https://astro.build/config
export default defineConfig({
  site: SITE,
  // Internationalisation : anglais à la racine, /es/ et /fr/ pour les autres.
  i18n: {
    locales: ['en', 'es', 'fr'],
    defaultLocale: 'en',
    routing: {
      prefixDefaultLocale: false,
    },
  },
  integrations: [
    sitemap({
      i18n: {
        defaultLocale: 'en',
        locales: { en: 'en-US', es: 'es-ES', fr: 'fr-FR' },
      },
    }),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
});
