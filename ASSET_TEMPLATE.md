---
# ============================================================================
#  MODÈLE D'ASSET — copie ce fichier dans  src/content/assets/  puis renomme-le
#  (ex. src/content/assets/mon-super-pack.md). Le nom du fichier = l'URL.
#
#  SEULS  title  ET  tagline  SONT OBLIGATOIRES.
#  Tout le reste est optionnel : supprime une ligne que tu n'utilises pas et
#  la section correspondante disparaît proprement du site.
# ============================================================================

# --- Obligatoire ---
title: Nom de ton pack
tagline: Une phrase d'accroche courte qui décrit le pack.

# --- Visibilité / ordre (optionnel) ---
draft: false        # true = caché du site (brouillon)
featured: false     # true = mis en avant, grande carte en haut de l'accueil
order: 0            # tri : plus le nombre est grand, plus l'asset apparaît haut
date: 2026-07-23

# --- Classification (optionnel) ---
category: Environment          # ex. Environment, Props, Modular Kit, Vehicles
engine: Unreal Engine 5.8
tags: [stylized, modular, unreal, game-ready]

# --- Traductions (optionnel) : titre / accroche / features par langue ---
# Si tu ne mets rien, la version par défaut (ci-dessus) s'affiche dans toutes
# les langues. Renseigne seulement ce que tu veux traduire.
# i18n:
#   es:
#     title: Título en español
#     tagline: Frase de enganche en español
#     features: [Punto 1, Punto 2]
#   fr:
#     title: Titre en français
#     tagline: Accroche en français
#     features: [Point 1, Point 2]

# --- Média (tout optionnel) ---
# Dépose tes images dans  src/content/assets/media/  et pointe-les ici.
# Sans cover : un joli placeholder de marque (cube) s'affiche à la place.
cover: ./media/mon-pack-cover.png
# banner : image utilisée par le carrousel d'accueil si l'asset est featured.
# Si absent, l'accueil prend la 1re image de gallery (JAMAIS la cover, souvent
# typographiée, elle rend mal recadrée en bannière).
# banner: ./media/mon-pack-banner.png
gallery:
  - ./media/mon-pack-1.png
  - ./media/mon-pack-2.png
# youtube : ID ou URL. Présent -> une vidéo remplace la cover en tête de fiche.
# youtube: dQw4w9WgXcQ
# playableDemoUrl : SEULEMENT si tu as une vraie démo jouable en ligne (itch.io…).
# playableDemoUrl: https://ton-compte.itch.io/ton-pack
demoMapIncluded: false      # true si une map de démo est LIVRÉE dans le pack
overviewMapIncluded: false  # true si la planche Overview est LIVRÉE

# --- Commercial (optionnel) ---
fabUrl: https://www.fab.com/listings/ton-listing   # bouton « Get it on Fab »
pricePersonal: "$29"
pricePro: "$89"
license: Standard License

# --- Features : 5 à 8 puces (optionnel) ---
features:
  - Première caractéristique concrète
  - Deuxième caractéristique
  - Troisième caractéristique

# --- Specs techniques (optionnel, chaque ligne vide est masquée) ---
# ⚠️ N'indique QUE des valeurs réellement mesurées dans ton pack.
specs:
  formats: [Unreal project, GLB, Blender]
  meshes: 0
  triangles: "0"
  materials: 0
  textures: 0
  textureRes: up to 2K
  collision: Custom UCX
  lods: 0–3
  nanite: false
  animated: ""          # méthode réelle si animé (ex. "Blueprint-driven doors")
  rigged: false
  characters: 0
---

Écris ici la description longue de ton pack, en **Markdown**.

Tu peux utiliser des sous-titres, du **gras**, des listes, des liens.
Décris une seule fois le style et la palette visibles (ex. « stylized low-poly,
collines vertes, façades neutres »), puis ce que l'acheteur peut construire.
