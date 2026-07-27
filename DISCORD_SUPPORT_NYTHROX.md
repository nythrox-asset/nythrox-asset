# Serveur Discord de support Nythrox — plan de montage

Je ne peux pas créer le serveur à ta place, ça demande d'agir sur ton compte.
Voici le serveur prêt à monter. Compte 15 à 20 minutes.

Principe directeur : **un acheteur doit pouvoir poser sa question en moins de
30 secondes, sans se demander où**. Tout le reste est secondaire. Un serveur
avec 30 salons vides fait plus de mal qu'un serveur avec 8 salons vivants.

---

## 1. Créer le serveur

Discord, bouton `+` à gauche, **Créer mon propre serveur**, puis
**Pour un club ou une communauté**.

- **Nom** : `Nythrox` (pas « Nythrox Support », le serveur sert aussi aux annonces)
- **Icône** : `public/branding/nythrox_logo_transparent.png` de ce dépôt
- **Langue du serveur** : English. Ta clientèle Fab est internationale.

Dans **Paramètres du serveur → Activer le mode Communauté**. Ça débloque les
salons d'annonces, les règles et l'AutoMod, et ça te fera gagner du temps.

---

## 2. Structure des salons

Volontairement courte. Chaque salon a une raison d'exister.

```
📣 INFORMATION
   #welcome            lecture seule, règles + comment demander de l'aide
   #announcements      salon d'ANNONCES (les gens peuvent s'y abonner)
   #changelog          une entrée par version publiée

🛠 SUPPORT
   #support-en         support en anglais
   #support-fr         support en français
   #bug-reports        forum, un fil par bug
   #feature-requests   forum, un fil par idée, avec votes

🎨 COMMUNITY
   #showcase           ce que les gens construisent avec tes packs
   #general            discussion libre
```

**Pourquoi des forums pour les bugs et les demandes.** Un salon de discussion
classique noie un bug signalé il y a trois jours. Un forum garde un fil par
sujet, avec un état, et tu peux le marquer résolu. Discord → clic droit sur la
catégorie → Créer un salon → **Forum**.

Balises à créer dans `#bug-reports` : `Door System`, `Selection & Assembly`,
`Asset pack`, `Confirmé`, `Corrigé`, `Pas reproductible`.

---

## 3. Rôles

```
@Nythrox        toi. Administrateur.
@Verified buyer attribué à la main après vérification de la commande Fab
@Member         tout le monde à l'arrivée
```

**Ne complique pas.** Un rôle acheteur vérifié suffit à faire la différence
entre une question de curieux et une demande d'un client, et c'est ce qui
justifie que tu répondes en priorité. Pour le vérifier : demande la référence
de commande Fab en message privé, jamais en public.

---

## 4. Permissions, le strict nécessaire

Pour `#welcome`, `#announcements` et `#changelog`, retire à `@everyone` le droit
**Envoyer des messages**. Ce sont des salons de diffusion.

Partout ailleurs, laisse `@everyone` écrire. Un support fermé n'est pas un
support.

Retire à `@everyone`, sur tout le serveur : **Mentionner @everyone**,
**Gérer les messages**, **Gérer les fils**.

---

## 5. Le message de #welcome, à copier tel quel

> **Welcome to Nythrox.**
> Environments, modular kits and tools for Unreal Engine.
>
> **Need help?** Post in `#support-en` or `#support-fr`.
> Found a bug? Open a thread in `#bug-reports`.
>
> **To get a useful answer on the first try, include:**
> • your Unreal Engine version, and the exact product version
> • what you did, what you expected, what happened instead
> • a screenshot, and the Output Log if something failed
> • whether it also happens in a brand new empty project
>
> **House rules**
> 1. One topic per thread. It keeps answers findable for the next person.
> 2. No piracy, no asking for or sharing purchased files. Instant ban.
> 3. Be civil. Nobody here owes you anything.
> 4. Custom development requests go to DM, not the support channels.
>
> Typical first answer within 48h, weekends included but slower.

---

## 6. AutoMod, trois règles qui suffisent

Paramètres du serveur → **AutoMod**.

1. **Bloquer les liens d'invitation Discord** — évite le démarchage.
2. **Bloquer le spam** — règle intégrée, active-la telle quelle.
3. **Mots bloqués** : `free download`, `crack`, `cracked`, `torrent`, `nulled`.
   Action : bloquer le message et t'alerter.

---

## 7. Après la création, ce qui compte vraiment

**Génère une invitation permanente.** Clic droit sur le serveur →
**Inviter des personnes** → **Modifier le lien d'invitation** →
Expire **Jamais**, Nombre max d'utilisations **Aucune limite**.

Une invitation par défaut expire en 7 jours. Si tu colles celle-là sur Fab, ton
lien de support sera mort la semaine suivante, et tes acheteurs tomberont sur
une page d'erreur. C'est l'erreur la plus fréquente et la plus coûteuse.

**Puis colle ce lien à deux endroits :**

1. dans `src/site.ts` de ce dépôt, champ `support.discordInvite` ;
2. dans le champ Support de tes fiches Fab.

Dès que le champ est rempli, la page `/support` affiche le bouton à la place du
message « bientôt disponible ». Rien d'autre à faire.

---

## 8. Ce que je n'ai pas mis, et pourquoi

- **Pas de bot de tickets.** Utile à partir de plusieurs dizaines de demandes
  par semaine. En dessous, un forum fait le même travail sans dépendance.
- **Pas de salon par produit.** Tu en as deux. Les balises du forum suffisent
  et évitent des salons déserts, qui donnent l'impression d'un produit mort.
- **Pas de vérification automatique des achats.** Fab ne fournit pas d'API
  publique pour ça aujourd'hui, à vérifier avant de promettre quoi que ce soit
  à tes clients.
