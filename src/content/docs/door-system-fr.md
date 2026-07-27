---
title: Interactive Door System
source: README.md
version: Nythrox Interactive Door System 1.4.0
---

## Nouveautés de la 1.4.0

- La charnière virtuelle pivote désormais sur la face du battant côté
  ouverture, comme un vrai nœud de charnière (**Hinge At Leaf Face**, activé
  par défaut). Cela prolonge l'affinage de la charnière commencé avec le
  **Retrait de charnière** de la 1.3.2 : le retrait déplace le pivot le long
  de la largeur de la porte, l'option de face du battant supprime le décalage
  à mi-épaisseur qui détachait visiblement les battants épais de leur dormant.
- Nouveau placement de charnière **Demonstrated** : la porte tourne autour du
  centre exact du mouvement enregistré entre fermée et ouverte, et reproduit
  parfaitement la pose enregistrée même sur des meshes aux bounds sans
  signification.
- **Sons** d'ouverture, de fermeture et de porte verrouillée, avec un contrôle
  de volume.
- **Événements Blueprint** : On Door Opened, On Door Closed et
  On Door Interaction Denied.
- **Verrouillage** : une porte verrouillée refuse l'interaction, joue le son
  de porte verrouillée et déclenche l'événement de refus.
- **Fermeture automatique** après un délai configurable.
- **Easing** du mouvement : Ease In Out par défaut pour une sensation de porte
  poussée à la main ; Linear et Ease Out sont disponibles.
- **Portes liées** : les doubles portes et les sas s'ouvrent et se ferment
  ensemble.
- **État de porte répliqué** pour les jeux en réseau, serveur autoritaire
  (voir la section Multijoueur, y compris son unique limitation honnête).
- Bouton **Détecter le cadre** : un clic mesure le montant réel de l'ouverture
  et règle le Retrait de charnière en conséquence.
- Le panneau n'écrase plus les réglages modifiés en dehors de lui (panneau
  Details, scripts, undo) et s'actualise automatiquement quand la sélection de
  l'éditeur change.

## Mise à jour depuis la 1.3.x

Les portes créées en 1.3.x se chargent et fonctionnent sans réenregistrer les
poses. Deux nouveaux défauts changent volontairement le mouvement des portes
existantes :

- L'easing vaut désormais **Ease In Out** par défaut. Réglez **Ease Mode** sur
  Linear sur le composant de la porte pour retrouver le mouvement exact de la
  1.3.x.
- La charnière pivote désormais à la face du battant par défaut. Désactivez
  **Hinge At Leaf Face** sur le composant de la porte pour retrouver l'ancien
  pivot à mi-épaisseur.

Tout le reste (poses enregistrées, réglages de l'indicateur, côté de
charnière, retrait de charnière) est conservé tel quel.

## Installation

1. Fermez Unreal Editor.
2. Copiez le dossier complet `NythroxDoorSystem` dans
   `<VotreProjet>/Plugins/`.
3. Ouvrez le projet, activez **Nythrox Interactive Door** si Unreal le
   demande, puis redémarrez l'éditeur.
4. Ouvrez **Tools > Nythrox Porte interactive**.

Le plugin contient un module Editor et un module Runtime. Une porte interactive
a besoin du Runtime dans le jeu final. L'archive contient les DLL Editor Win64
et les sources C++ ; le packaging d'un jeu peut compiler le module Runtime pour
la configuration choisie.

## Avant de créer la porte

Sélectionnez seulement les parties mobiles de la porte et leurs
meshes/composants de collision. Ne sélectionnez ni le mur, ni le dormant, ni
le sol, ni une géométrie fixe voisine. Pour une double porte, créez deux portes
indépendantes, puis ajoutez chaque battant à la liste **Linked Doors** de
l'autre sur le composant de porte, pour que les deux battants s'ouvrent et se
ferment ensemble.

## Réglages

| Contrôle | Défaut | Effet |
|---|---:|---|
| Touche d'interaction | E | Touche affichée et utilisée pour l'interaction. |
| Distance (cm) | 250 | Distance maximale entre le joueur et les bounds visibles. |
| Durée du mouvement (s) | 0,65 | Durée de l'ouverture/fermeture. |
| Décalage vertical de l'indicateur (cm) | 0 | Décalage signé depuis le centre des bounds visibles. |
| Arête de charnière | Automatique | Charnière virtuelle Automatique, Gauche ou Droite. |
| Retrait de charnière (cm) | 0 | Déplace la charnière virtuelle vers l'intérieur du battant ; une valeur négative la déplace vers l'extérieur. |
| Détecter le cadre (bouton) | - | Mesure le montant réel de l'ouverture autour de la porte sélectionnée et règle le Retrait de charnière sur cette valeur. Rien ne change si aucun mur n'est trouvé. |
| Tourner autour de l'arête de la porte | Activé | Utilise la charnière virtuelle pour une porte battante. |
| Afficher l'indicateur [touche] en jeu | Activé | Affiche le prompt localisé à portée. |
| Commence ouverte | Désactivé | Démarre le jeu dans la pose ouverte enregistrée. |

Le panneau s'actualise automatiquement quand la sélection de l'éditeur change.
Cliquez sur **Actualiser** pour forcer à tout moment un recomptage des
composants mesh et des collisions sélectionnés.

**Détecter le cadre** mesure l'ouverture en scannant les boîtes englobantes
monde (AABB) des acteurs Static Mesh qui encadrent le battant. Il n'utilise
volontairement pas de line trace : les meshes visuels produits par le pipeline
d'export Roblox n'ont aucune collision (NoCollision), un trace ne toucherait
donc rien, ou toucherait un proxy grossier au lieu du mur visible. Les
morceaux de mur de part et d'autre du battant doivent donc être des acteurs
Static Mesh dont les bounds atteignent l'ouverture. Si aucun mur adjacent
n'est trouvé, le Retrait de charnière reste inchangé.

## Procédure guidée

1. Sélectionnez tous les meshes visuels mobiles et leurs collisions.
2. Réglez les options puis cliquez sur **Créer la porte**. L'outil crée
   `BP_InteractiveDoor`, remplace les sources, rend les composants Movable et
   enregistre déjà la pose fermée initiale.
3. Corrigez éventuellement la transform fermée de l'acteur entier, puis
   cliquez sur **Enregistrer fermée**.
4. Déplacez et/ou faites pivoter l'acteur entier vers sa pose ouverte, puis
   cliquez sur **Enregistrer ouverte**. La porte revient automatiquement à la
   pose fermée.
5. Utilisez **Aperçu fermée**, **Aperçu ouverte** ou **Tester l'animation**
   sans lancer le jeu.
6. Si Automatique choisit le mauvais côté, forcez Gauche ou Droite puis
   retestez.
7. Si le battant dépasse dans le mur, cliquez sur **Détecter le cadre** pour
   mesurer automatiquement le montant réel, ou augmentez **Retrait de
   charnière** manuellement jusqu'à aligner le pivot virtuel sur le montant
   visible. L'aperçu applique immédiatement la valeur ; il n'est pas
   nécessaire de réenregistrer la pose ouverte.
8. En mode Play, approchez-vous et appuyez sur la touche configurée.

**Annuler la porte** restaure les acteurs sources de la dernière création tant
que ses données d'opération existent. L'Undo normal d'Unreal reste aussi
disponible pour la transaction active.

## Fonctionnement de l'arête de charnière

L'outil ne déplace pas et ne corrige pas le pivot importé du mesh. Il repère la
plus grande dalle visible de la porte, détecte ses deux arêtes verticales et
construit une charnière virtuelle sur le côté choisi.

- **Automatique** compare la pose ouverte enregistrée aux deux arcs possibles.
- **Gauche** et **Droite** forcent une arête si l'aperçu automatique est faux.
- **Retrait de charnière** décale l'arête résolue vers le centre du battant en
  centimètres monde. Une valeur négative la décale hors du battant. `0`
  conserve exactement le comportement historique.
- **Hinge At Leaf Face** (réglage du composant, activé par défaut depuis la
  1.4.0) déplace le pivot de la mi-épaisseur vers la face du battant côté
  ouverture, comme un vrai nœud de charnière. Sur les battants épais, le pivot
  à mi-épaisseur détachait visiblement le battant ouvert de son dormant ;
  désactivez l'option pour le retrouver.
- **Hinge Placement** réglé sur **Demonstrated** (réglage du composant) saute
  entièrement la détection d'arête et fait tourner la porte autour du centre
  exact du mouvement enregistré entre fermée et ouverte. Si la pose ouverte a
  été placée précisément, il la reproduit parfaitement et fonctionne même
  quand les bounds du mesh n'ont aucun sens (cubes placeholder). Il retombe
  sur l'arête détectée du battant quand la rotation enregistrée est inférieure
  à environ `2` degrés.
- Au-delà d'environ `0,5°` de rotation, le centre de la porte suit un arc
  circulaire autour de l'arête.
- Sans rotation significative, le déplacement linéaire exact est conservé,
  ce qui convient aux portes coulissantes.
- Si aucune arête fiable n'est détectée, le système revient à l'interpolation
  classique des transforms.

La porte fonctionne donc même avec un mauvais pivot, et son centre ne suit
plus une ligne droite qui traverse le mur au milieu de l'animation.

## Portes coulissantes

La même procédure prend en charge les portes qui se translatent au lieu de
tourner. Enregistrez la pose ouverte en déplaçant l'acteur de la porte sans le
faire pivoter (toute rotation inférieure à `0,5` degré compte comme nulle) :
le composant saute alors la charnière virtuelle et interpole linéairement la
translation enregistrée, avec l'easing choisi toujours appliqué. Aucun réglage
de charnière n'est nécessaire pour une porte coulissante, et deux panneaux
coulissants peuvent être liés avec **Linked Doors** comme n'importe quelle
double porte.

## Réglages du composant ajoutés en 1.4.0

Tous les nouveaux réglages vivent sur le `NythroxDoorComponent` du Blueprint
de la porte (`BP_InteractiveDoor`), dans le panneau Details sous la catégorie
indiquée. Chacun d'eux est aussi lisible et modifiable depuis Blueprint.

| Propriété | Catégorie | Défaut | Effet |
|---|---|---:|---|
| Locked (`bLocked`) | Nythrox Door > Interaction | Désactivé | Une porte verrouillée refuse l'interaction, joue Locked Sound et déclenche On Door Interaction Denied. Le verrou ne déplace pas la porte. |
| Auto Close Delay (`AutoCloseDelay`) | Nythrox Door > Interaction | 0 s | Nombre de secondes pendant lesquelles la porte reste complètement ouverte avant de se refermer seule. `0` signifie jamais. |
| Linked Doors (`LinkedDoors`) | Nythrox Door > Interaction | vide | Autres acteurs de porte basculés en même temps que celle-ci (doubles portes, sas). Les liens ne sont pas suivis transitivement : deux battants peuvent simplement se référencer l'un l'autre. |
| Ease Mode (`EaseMode`) | Nythrox Door > Motion | Ease In Out | Easing appliqué au mouvement d'ouverture/fermeture : Linear, Ease Out ou Ease In Out. Ease In Out donne la sensation d'une porte poussée à la main. |
| Ease Exponent (`EaseExponent`) | Nythrox Door > Motion | 2.0 | Force de la courbe d'easing, de `1` (presque linéaire) à `5`. |
| Hinge Placement (`HingePlacement`) | Nythrox Door > Motion | Slab Edge (détectée) | Slab Edge utilise l'arête de porte détectée, affinée par Retrait de charnière et Hinge At Leaf Face. Demonstrated utilise le centre exact de rotation des poses enregistrées. |
| Hinge At Leaf Face (`bHingeAtLeafFace`) | Nythrox Door > Motion | Activé | Place la charnière sur la face du battant côté ouverture au lieu de la mi-épaisseur. Désactivez pour retrouver le pivot de la 1.3.x. |
| Open Sound (`OpenSound`) | Nythrox Door > Audio | None | Joué à l'emplacement de la porte quand elle commence à s'ouvrir. |
| Close Sound (`CloseSound`) | Nythrox Door > Audio | None | Joué à l'emplacement de la porte quand elle commence à se fermer. |
| Locked Sound (`LockedSound`) | Nythrox Door > Audio | None | Joué quand l'interaction est refusée parce que la porte est verrouillée. |
| Sound Volume (`SoundVolume`) | Nythrox Door > Audio | 1.0 | Multiplicateur de volume des trois sons, de `0` à `2`. `0` les coupe. |
| Replicate Door State (`bReplicateDoorState`) | Nythrox Door > Network | Activé | Réplique l'état ouvert/fermé vers les clients dans les jeux en réseau ; le serveur reste autoritaire. Voir Multijoueur. |

Le composant expose aussi trois événements assignables sous
**Nythrox Door > Events** :

- **On Door Opened** : déclenché quand la porte finit de s'ouvrir (en jeu
  uniquement).
- **On Door Closed** : déclenché quand la porte finit de se fermer (en jeu
  uniquement).
- **On Door Interaction Denied** : déclenché quand l'interaction est refusée
  parce que la porte est verrouillée.

Les sons et les événements se déclenchent en jeu, pas pendant les aperçus de
l'éditeur.

## Multijoueur

Avec **Replicate Door State** activé (le défaut), l'état ouvert/fermé de la
porte est répliqué du serveur vers chaque client. Le serveur est autoritaire ;
chaque machine anime le mouvement localement et joue ses propres sons et
événements. L'hôte d'un listen server interagit avec les portes sans rien
configurer, puisque l'hôte est le serveur.

La limitation honnête : une porte posée dans le niveau n'a pas de connexion
propriétaire (owning connection), donc une interaction déclenchée sur un
client distant ne peut pas atteindre le serveur par le composant de porte
lui-même. Faites passer la requête par un acteur que le client possède ;
c'est une ligne de Blueprint : sur le Character ou le PlayerController de
votre jeu, un custom event Run on Server qui appelle `SetDoorOpen` ou
`ToggleDoor` sur la porte. L'état résultant se réplique ensuite
automatiquement vers tous les clients.

Deux remarques liées :

- Le polling intégré de la touche `[E]` utilise le premier Player Controller
  local. Sur un client distant, il déclenche l'interaction localement, ce qui,
  comme expliqué ci-dessus, ne peut pas atteindre le serveur tout seul ;
  utilisez le routage Blueprint pour les portes pilotées par les clients dans
  les jeux en réseau.
- `Locked` est une propriété simple et n'est pas répliquée. Dans les jeux en
  réseau, réglez-la côté serveur (ou sur chaque machine) et faites passer les
  interactions par `TryInteract` pour que le verrou soit respecté.

## Affichage de l'indicateur

Le prompt est toujours rendu en screen space, centré sur les bounds visibles,
avec le décalage vertical signé choisi. La porte ne peut donc plus masquer ni
découper le texte.

Le texte Runtime suit l'anglais, le français, l'allemand ou l'espagnol et
affiche la touche choisie : par exemple `[E] Ouvrir` ou `[E] Fermer`. Une autre
langue utilise l'anglais par défaut.

## Sauvegarder une porte interactive ou statique

| Garder l'animation interactive | Résultat de Sauvegarder la porte |
|---|---|
| Activé | Sauvegarde le Blueprint interactif existant avec son Runtime, ses poses, son prompt et sa touche. |
| Désactivé | Crée un `BP_StaticDoor` séparé avec meshes, matériaux, transforms et collisions, sans Runtime, prompt ni interaction. |

La sauvegarde statique ne supprime pas et ne convertit pas la porte interactive
déjà placée dans la scène. Pour enregistrer une porte statique fermée, cliquez
sur **Aperçu fermée** avant **Sauvegarder la porte**.

## Collisions et comportement Runtime

- Les Static Mesh Components sélectionnés, y compris les composants cachés
  `RBX_OWNED_COLLISION`, se déplacent avec la porte.
- Leurs profils de collision et collisions actives sont conservés.
- Le mouvement utilise une transform de type téléportation, sans sweep : la
  porte ne s'arrête pas automatiquement contre un joueur ou un obstacle.
- La distance d'interaction est calculée vers les bounds visibles, pas vers le
  pivot de l'acteur ou du mesh.
- Le Runtime utilise le premier Player Controller local pour la touche
  d'interaction. La réplication de l'état des portes pour les jeux en réseau
  est décrite dans la section Multijoueur, y compris la façon dont un client
  distant doit router son interaction.

## API Blueprint

Le composant Runtime expose :

- `TryInteract` pour un système d'input personnalisé ; il respecte `Locked`
  et déclenche On Door Interaction Denied en cas de refus ;
- `ToggleDoor` pour alterner ouverte/fermée ;
- `SetDoorOpen` pour demander un état précis ;
- `IsDoorOpen` pour lire l'état courant ;
- `SetLocked` et `IsLocked` pour contrôler et lire le verrou sans déplacer la
  porte ;
- les événements assignables On Door Opened, On Door Closed et
  On Door Interaction Denied (voir Réglages du composant ajoutés en 1.4.0).

## Portes existantes et panneau

Les champs du panneau sont entièrement appliqués à la création. Sur une porte
déjà créée, modifiez les valeurs Runtime générales dans son composant, panneau
Details. Le choix de charnière est également relu et appliqué par le panneau
Nythrox lors des aperçus et enregistrements.

Depuis la 1.4.0, le panneau s'actualise automatiquement quand la sélection de
l'éditeur change, et ses commandes n'écrivent que les champs de charnière que
vous avez réellement modifiés depuis la dernière actualisation. Une valeur
changée entre-temps ailleurs (panneau Details, un script, un autre outil ou un
undo) est relue au lieu d'être écrasée par une copie périmée du panneau.

Les anciennes portes sans donnée de charnière choisissent automatiquement une
arête au Runtime. Les anciens prompts enregistrés en world space sont forcés
en screen space lisible.

## Limites et dépannage

| Problème | Vérification |
|---|---|
| Le panneau n'apparaît pas | Activez le plugin, redémarrez Unreal, puis ouvrez Tools. |
| Créer la porte est désactivé | Sélectionnez uniquement des Static Mesh actors/composants mobiles valides puis cliquez sur Actualiser. |
| La porte ouvre du mauvais côté | Forcez Gauche ou Droite, puis utilisez Tester l'animation. |
| La charnière est dans le mur | Cliquez sur Détecter le cadre, ou augmentez Retrait de charnière jusqu'à ce que l'aperçu pivote sur le montant visible. Il n'est pas nécessaire de réenregistrer la pose ouverte. |
| Détecter le cadre ne trouve aucun mur | Le scan utilise les boîtes englobantes (AABB) des acteurs Static Mesh, pas des traces. Les morceaux de mur de part et d'autre du battant doivent être des acteurs Static Mesh dont les bounds atteignent l'ouverture. |
| La touche ne fait rien | Vérifiez le mode Play, la distance d'interaction, la touche configurée, que le plugin Runtime est activé et que Locked est désactivé. |
| La porte refuse de s'ouvrir et joue un son | La porte est Locked ; appelez SetLocked(false) ou décochez le drapeau sur le composant. |
| Le mouvement est différent après la mise à jour | Voir Mise à jour depuis la 1.3.x : réglez Ease Mode sur Linear et/ou désactivez Hinge At Leaf Face. |
| Un client distant ne peut pas ouvrir la porte | Comportement attendu pour une porte posée dans le niveau ; routez l'interaction par le serveur comme montré dans la section Multijoueur. |
| Le prompt est trop haut/bas | Modifiez le décalage vertical, positif ou négatif. |
| La porte statique est sauvegardée ouverte | Faites Aperçu fermée avant la sauvegarde statique. |

Menus, panneau et prompt Runtime prennent en charge l'anglais, le français,
l'allemand et l'espagnol. Quelques notifications Python peuvent rester en
français ou en anglais.
