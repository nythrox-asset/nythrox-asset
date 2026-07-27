import { ui, defaultLang, type Lang, type UIKey } from './ui';

/** Convertit un `Astro.currentLocale` (string | undefined) en Lang sûr. */
export function toLang(locale: string | undefined): Lang {
  if (locale === 'es' || locale === 'fr') return locale;
  return defaultLang;
}

/** Renvoie une fonction de traduction t('cle', { var }). */
export function useTranslations(lang: Lang) {
  return function t(key: UIKey, vars?: Record<string, string | number>): string {
    let str: string = (ui[lang]?.[key] ?? ui[defaultLang][key] ?? key) as string;
    if (vars) {
      for (const [k, v] of Object.entries(vars)) {
        str = str.split(`{${k}}`).join(String(v));
      }
    }
    return str;
  };
}

/** Préfixe d'URL d'une langue : '' pour l'anglais, '/es', '/fr'. */
export function langPrefix(lang: Lang): string {
  return lang === defaultLang ? '' : `/${lang}`;
}

/** Retire un éventuel préfixe /es ou /fr d'un chemin. */
export function stripLangPrefix(pathname: string): string {
  const m = pathname.match(/^\/(es|fr)(\/|$)/);
  if (m) return pathname.slice(m[1].length + 1) || '/';
  return pathname;
}

/** Même chemin dans une autre langue (pour le sélecteur + hreflang). */
export function localizePath(pathname: string, lang: Lang): string {
  const bare = stripLangPrefix(pathname);
  let p = langPrefix(lang) + bare;
  if (!p.startsWith('/')) p = '/' + p;
  if (p !== '/' && !p.endsWith('/')) p += '/';
  return p.replace(/\/{2,}/g, '/');
}

/** Lien vers une fiche asset dans la langue courante. */
export function assetHref(lang: Lang, id: string): string {
  return `${langPrefix(lang)}/assets/${id}/`;
}

/** Lien vers l'accueil dans la langue courante. */
export function homeHref(lang: Lang): string {
  return langPrefix(lang) === '' ? '/' : `${langPrefix(lang)}/`;
}

/* ------------------------------------------------------------------ *
 *  Contenu d'asset localisé : renvoie la version traduite d'un champ  *
 *  si elle existe dans frontmatter `i18n.<lang>`, sinon la valeur par  *
 *  défaut (repli automatique).                                        *
 * ------------------------------------------------------------------ */
type LocaleFields = {
  title?: string;
  tagline?: string;
  intro?: string;
  features?: string[];
  includes?: string;
  notes?: string;
  idealFor?: string;
};
type AssetData = {
  title: string;
  tagline: string;
  intro?: string;
  features: string[];
  includes?: string;
  notes?: string;
  idealFor?: string;
  i18n?: Partial<Record<'es' | 'fr', LocaleFields>>;
};

export function localizedContent(data: AssetData, lang: Lang) {
  const o = lang !== 'en' ? data.i18n?.[lang] : undefined;
  return {
    title: o?.title ?? data.title,
    tagline: o?.tagline ?? data.tagline,
    intro: o?.intro ?? data.intro,
    features: o?.features ?? data.features,
    includes: o?.includes ?? data.includes,
    notes: o?.notes ?? data.notes,
    idealFor: o?.idealFor ?? data.idealFor,
  };
}

export type { Lang, UIKey };
