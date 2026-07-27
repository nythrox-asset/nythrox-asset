import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

/* Traduction optionnelle des textes humains d'un asset (par langue). */
const localeOverride = z.object({
  title: z.string().optional(),
  tagline: z.string().optional(),
  intro: z.string().optional(), // paragraphe d'accroche long
  features: z.array(z.string()).optional(),
  includes: z.string().optional(), // ligne "Includes: ..."
  notes: z.string().optional(), // "Important notes: ..."
  idealFor: z.string().optional(), // "Ideal for: ..."
});

/* ------------------------------------------------------------------ *
 *  Collection « assets »                                              *
 *  Un fichier .md par asset dans src/content/assets/.                 *
 *                                                                     *
 *  Presque TOUT est optionnel : si tu ne renseignes pas un champ,     *
 *  la section correspondante ne s'affiche simplement pas — la fiche   *
 *  reste équilibrée et belle. Seuls `title` et `tagline` sont requis. *
 * ------------------------------------------------------------------ */

const assets = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/assets' }),
  schema: ({ image }) =>
    z.object({
      /* --- Requis --- */
      title: z.string(),
      tagline: z.string(), // une phrase d'accroche courte

      /* --- Visibilité / ordre --- */
      draft: z.boolean().default(false), // true = caché du site
      featured: z.boolean().default(false), // mis en avant en haut de l'accueil
      order: z.number().default(0), // tri (plus grand = plus haut)
      date: z.coerce.date().optional(),

      /* --- Classification --- */
      category: z.string().optional(), // ex. "Environment", "Props", "Modular Kit"
      engine: z.string().optional(), // ex. "Unreal Engine 5.8"
      tags: z.array(z.string()).default([]),

      /* --- Média (tous optionnels : sans image → placeholder de marque) --- */
      cover: image().optional(), // grande image de tête + carte
      banner: image().optional(), // image bannière d'accueil (sinon 1re de gallery, JAMAIS la cover à texte)
      gallery: z.array(image()).default([]), // captures supplémentaires
      youtube: z.string().optional(), // ID ou URL YouTube → section vidéo
      playableDemoUrl: z.string().url().optional(), // vraie démo jouable en ligne
      demoDownloadUrl: z.string().optional(), // fichier de démo à télécharger (chemin relatif ou URL)
      demoDownloadNote: z.string().optional(), // ex. "Windows · 450 MB"
      demoMapIncluded: z.boolean().default(false), // map de démo LIVRÉE dans le pack
      overviewMapIncluded: z.boolean().default(false), // planche Overview LIVRÉE

      /* --- Commercial --- */
      fabUrl: z.string().url().optional(), // lien de ta fiche Fab (bouton d'achat)
      pricePersonal: z.string().optional(), // ex. "$29"
      pricePro: z.string().optional(), // ex. "$89"
      license: z.string().optional(), // ex. "Standard License"

      /* --- Contenu --- */
      intro: z.string().optional(), // paragraphe d'accroche (sinon corps markdown)
      features: z.array(z.string()).default([]), // 5–8 puces
      includes: z.string().optional(), // ligne "Includes: ..."
      notes: z.string().optional(), // "Important notes: ..."
      idealFor: z.string().optional(), // "Ideal for: ..."

      /* --- Traductions optionnelles (repli auto sur les champs par défaut) --- */
      i18n: z
        .object({
          es: localeOverride.optional(),
          fr: localeOverride.optional(),
        })
        .optional(),

      /* --- Specs techniques (chaque champ vide = ligne masquée) --- */
      specs: z
        .object({
          formats: z.array(z.string()).optional(), // ["Unreal project", "GLB", "Blender"]
          meshes: z.number().optional(),
          triangles: z.string().optional(), // texte libre ("1.2M")
          materials: z.number().optional(),
          textures: z.number().optional(),
          textureRes: z.string().optional(), // "up to 2K"
          collision: z.string().optional(), // "Custom UCX" / "Auto-generated" / "None"
          lods: z.string().optional(), // "0–3" / "None"
          nanite: z.boolean().optional(),
          rigged: z.boolean().optional(),
          animated: z.string().optional(), // méthode réelle: "Blueprint-driven doors"
          characters: z.number().optional(),
        })
        .optional(),
    }),
});

/* ------------------------------------------------------------------ *
 *  Collection « docs »                                                *
 *  Manuels des plugins, en ligne sur /docs/.                          *
 *                                                                     *
 *  Ces fichiers ne s'ecrivent PAS a la main : ils sont importes       *
 *  depuis le README livre dans le plugin, par                         *
 *  `scripts/importer_manuel_porte.py`. La source de verite reste le   *
 *  manuel que l'acheteur trouve dans son paquet, sinon la page en     *
 *  ligne et le fichier livre divergent des la premiere version.       *
 *                                                                     *
 *  Convention de nom : <produit>-<langue>.md                          *
 * ------------------------------------------------------------------ */
const docs = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/docs' }),
  schema: z.object({
    title: z.string(),
    /** Fichier d'origine, pour retrouver d'ou vient le contenu. */
    source: z.string().optional(),
    /** Version du produit documentee, affichee sur la page. */
    version: z.string().optional(),
  }),
});

export const collections = { assets, docs };
