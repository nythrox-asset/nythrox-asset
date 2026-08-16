# Nythrox, vitrine Fab

Site vitrine statique (Astro) pour présenter tes packs d'assets et renvoyer vers
tes fiches **Fab**. Piloté par les données : **un fichier = un asset**, et tout
champ non renseigné disparaît proprement (une map sans vidéo reste une belle fiche).

Domaine de production : **nythrox-asset.com**

---

## Démarrer

```bash
npm install       # une seule fois
npm run dev        # aperçu en direct sur http://localhost:4321
npm run build      # génère le site final dans dist/
npm run preview    # prévisualise le build de production
```

---

## Ajouter un asset (le point important)

1. **Copie** `ASSET_TEMPLATE.md` dans `src/content/assets/` et **renomme-le**
   (ex. `src/content/assets/medieval-village.md`). Le nom du fichier devient
   l'URL : `/assets/medieval-village/`.
2. **Remplis les champs** en haut du fichier (le « frontmatter » entre les `---`).
   - Seuls `title` et `tagline` sont **obligatoires**.
   - Tout le reste est **optionnel** : supprime une ligne inutilisée et la
     section correspondante n'apparaît pas.
3. **Dépose tes images** dans `src/content/assets/media/` et pointe-les
   (`cover: ./media/mon-image.png`). Elles sont **optimisées automatiquement**
   (redimensionnées, WebP).
4. L'asset apparaît **tout seul** sur l'accueil et obtient sa page détail.

### Ce qui s'adapte automatiquement

| Si tu n'as pas… | Ce qui se passe |
|---|---|
| de `cover` | un placeholder de marque (cube cobalt) s'affiche à la place |
| de `youtube` | pas de bloc vidéo ; la cover (ou le placeholder) sert d'image de tête |
| de `playableDemoUrl` | pas de bouton « Play the demo » |
| de `gallery` | pas de section galerie |
| de `specs` | pas de tableau technique (et chaque ligne vide est masquée individuellement) |
| de `fabUrl` | le bouton d'achat affiche « Coming soon to Fab » |

> **Vidéo YouTube** : renseigne `youtube:` (ID ou URL) et une vidéo à chargement
> léger remplace la cover en tête de fiche. `playableDemoUrl` est réservé à une
> **vraie** démo jouable en ligne (itch.io, build web…), pas à une map livrée
> dans le pack. Pour ça, utilise `demoMapIncluded: true`.

---

## Langues (EN / ES / FR)

Le site est trilingue avec un **sélecteur à drapeaux** en haut à droite. URLs :

- Anglais (défaut) : `/` , `/assets/...`
- Espagnol : `/es/` , `/es/assets/...`
- Français : `/fr/` , `/fr/assets/...`

Balises `hreflang` générées automatiquement (bon pour le SEO), et le sélecteur
renvoie toujours vers la **même page** dans l'autre langue.

- **Traduire l'interface** (boutons, titres de sections, footer…) : `src/i18n/ui.ts`.
- **Traduire un asset** (titre / accroche / features) : ajoute un bloc `i18n:`
  dans son frontmatter (voir `ASSET_TEMPLATE.md`). Champ non traduit → repli
  automatique sur la version par défaut. La description longue (corps Markdown)
  reste dans la langue où tu l'as écrite.
- **Ajouter une langue** : ajoute son code dans `locales` (`astro.config.mjs`),
  une entrée dans `languages` + un bloc de traductions dans `src/i18n/ui.ts`,
  un drapeau dans `src/components/Flag.astro`, et les pages
  `src/pages/<code>/index.astro` + `src/pages/<code>/assets/[...slug].astro`
  (copie des versions `es/`).

## Personnaliser la marque

- **Couleurs, polices, rayons** : `src/styles/global.css`, bloc `@theme` en haut.
  Change une variable (ex. `--color-accent`) et tout le site suit.
- **Nom, accroche, lien du store Fab, réseaux** : `src/site.ts`.
- **Logos / favicon** : `public/branding/` et `public/favicon.ico`.
- **Image de partage par défaut** (aperçu réseaux) : `public/branding/og-default.png`.

---

## Déployer sur nythrox-asset.com

Le site est **100 % statique** (dossier `dist/`), hébergeable partout. Le domaine
perso `nythrox-asset.com` se branche chez n'importe quel hébergeur.

**Netlify / Vercel (le plus simple)**
1. Pousse ce dossier sur un repo GitHub (ou glisse-dépose `dist/` sur Netlify).
2. Build command : `npm run build` · Publish directory : `dist`.
3. Ajoute le domaine `nythrox-asset.com` dans les réglages du projet et suis les
   instructions DNS. Le fichier `public/CNAME` est ignoré par ces plateformes,
   sans effet, inoffensif.

**GitHub Pages**
1. Repo GitHub, active Pages (source : GitHub Actions, workflow Astro).
2. Le fichier `public/CNAME` (déjà présent, contient `nythrox-asset.com`)
   configure le domaine perso automatiquement.

Dans tous les cas, garde `site: 'https://nythrox-asset.com'` dans
`astro.config.mjs` (sert au sitemap et aux liens de partage).

---

## Structure

```
src/
  content/assets/        ← tes assets (1 .md chacun) + media/
  content.config.ts      ← schéma des champs (rarement à toucher)
  components/            ← briques d'UI (cartes, galerie, specs…)
  layouts/Base.astro     ← en-tête HTML, SEO, nav, footer
  pages/
    index.astro          ← accueil (héros + grille)
    assets/[...slug].astro ← page détail d'un asset
  styles/global.css      ← charte (couleurs, polices)
  site.ts                ← réglages globaux
public/                  ← logos, favicon, CNAME, robots.txt
ASSET_TEMPLATE.md        ← modèle à copier pour un nouvel asset
```

Les deux fichiers `stylized-town.md` et `minimal-sample.md` sont des **exemples** :
supprime-les une fois tes vrais assets ajoutés.
