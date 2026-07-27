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

Le **mode Communauté** est activé par le script, tu n'as rien à faire à la
main. Il débloque les salons d'annonces, auxquels d'autres serveurs peuvent
s'abonner, ainsi que les règles et l'AutoMod.

---

## 2. Structure des salons

Volontairement courte. Chaque salon a une raison d'exister.

```
📣 INFORMATION
   #welcome            lecture seule, règles + comment demander de l'aide
   #announcements      salon d'ANNONCES (les gens peuvent s'y abonner)
   #changelog          salon d'ANNONCES, une entrée par version publiée

🛠 SUPPORT
   #support-en         support en anglais
   #support-fr         support en français
   #bug-reports        forum, un fil par bug
   #feature-requests   forum, un fil par idée, avec votes

💬 COMMUNITY
   #showcase           ce que les ACHETEURS construisent avec tes packs
   #general            discussion libre

🔒 STAFF                (invisible pour @everyone)
   #server-updates     avis de modération envoyés par Discord
   #ticket-logs        transcriptions des tickets fermés
```

**Pourquoi `#welcome` n'est pas un salon d'annonces.** C'est lui qui sert de
salon de **règles** au sens de Discord, et Discord attend un salon texte
ordinaire à cet endroit. Personne ne s'abonne à des règles, la conversion
n'apporterait rien.

**Pourquoi la catégorie STAFF est privée.** `#server-updates` est le salon où
Discord dépose ses avis de modération. Ils te sont destinés, à toi seul, et
n'ont rien à faire sous les yeux de tes acheteurs. Son existence est une
condition obligatoire pour activer le mode Communauté.

**Pourquoi des forums pour les bugs et les demandes.** Un salon de discussion
classique noie un bug signalé il y a trois jours. Un forum garde un fil par
sujet, avec un état, et tu peux le marquer résolu. Discord → clic droit sur la
catégorie → Créer un salon → **Forum**.

Balises à créer dans `#bug-reports` : `Door System`, `Selection & Assembly`,
`Asset pack`, `Confirmé`, `Corrigé`, `Pas reproductible`.

---

## 3. Rôles

Les trois rôles sont créés par le script.

```
@Nythrox        toi. Affiché à part dans la liste des membres.
@Verified buyer attribué à la main après vérification de la commande Fab
@Member         rôle neutre, sans couleur ni mise en avant
```

**Ne complique pas.** Un rôle acheteur vérifié suffit à faire la différence
entre une question de curieux et une demande d'un client, et c'est ce qui
justifie que tu répondes en priorité. Pour le vérifier : demande la référence
de commande Fab en message privé, jamais en public.

Deux choses restent à faire à la main, parce qu'un bot ne peut pas les faire :

1. **Attribue-toi `@Nythrox`.** Le script crée le rôle mais ne peut pas te le
   donner : un bot ne peut pas modifier le propriétaire du serveur. Clic droit
   sur ton nom dans la liste des membres → Rôles → Nythrox. Sans ça, les
   acheteurs ne verront pas qui répond officiellement.
2. **Donne-lui les droits d'administration** si un jour tu ajoutes quelqu'un à
   ton support. Tant que tu es seul, ce n'est pas nécessaire : le propriétaire
   du serveur a tous les droits par construction.

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

## 6. AutoMod, quatre règles qui suffisent

Créées par le script, rien à cliquer. Tu les retrouves dans Paramètres du
serveur → AutoMod si tu veux les ajuster.

1. **Pas d'invitations** vers d'autres serveurs, ce qui évite le démarchage.
2. **Anti-spam**, la règle intégrée de Discord, entraînée sur son propre trafic.
3. **Pas de piratage** : `free download`, `cracked`, `torrent`, `nulled`,
   `keygen`, `warez`. Message bloqué et alerte dans `#server-updates`.
4. **Vagues de mentions** : un message citant plus de cinq personnes est bloqué.

Les alertes vont dans `#server-updates`, qui est privé. Une alerte de
modération affichée en public apprend surtout aux curieux quels mots
déclenchent quoi.

**Une seule chose à savoir si tu veux en ajouter** : Discord limite à six
règles à mots-clés par serveur, une seule anti-spam et une seule pour les
mentions. Le script en consomme deux sur six, une sur une et une sur une.

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

## 8. Tickets privés — Ticket Tool

Décision Nathan du 27/07/2026 : **Ticket Tool pour l'instant**, le bot maison
reste en réserve (voir la section 9).

Le forum public et les tickets privés ne font pas le même travail, et tu gardes
les deux. Le forum sert aux problèmes techniques, dont les réponses profitent
aux suivants. Le ticket privé sert à ce qui ne se dit pas en public :
facturation, licence, numéro de commande.

**Installation**

1. `tickettool.xyz` → Invite → choisis ton serveur.
2. Sur leur tableau de bord, crée un **panel** dans un salon `#open-a-ticket`
   que tu ajoutes à la catégorie SUPPORT.
3. Titre du panel : `Private ticket`.
   Description : `For invoicing, licensing or order questions. For technical
   problems, use the bug-reports forum instead: answers there help everyone.`

**Les causes du menu déroulant**

```
Door System            un problème sur le plugin de portes
Selection & Assembly   un problème sur le plugin d'assemblage
Asset pack             un problème sur un pack d'environnement
Invoicing / licence    facturation, licence, transfert
Other                  le reste
```

**Réglages qui comptent**

- Salon de transcription : choisis `#ticket-logs`, déjà créé par le script dans
  la catégorie STAFF et invisible pour les autres. Sans ce réglage, tu perds
  l'historique dès qu'un ticket est fermé.
- Rôle de support : `@Nythrox`. N'ajoute personne d'autre tant que tu es seul.
- Message d'ouverture automatique : reprends la liste « à joindre dès le
  premier message » de la section 5, ça t'évite un aller-retour à chaque fois.
- Limite d'un ticket ouvert par personne, pour éviter les doublons.

**La limite à connaître** : les causes ci-dessus se saisissent **à la main**
dans leur interface. Elles ne se synchronisent pas avec tes produits. Tu en
ajouteras une les deux ou trois fois par an où tu sors un produit. C'est le
prix à payer pour ne rien avoir à héberger ni maintenir.

---

## 9. En réserve : le bot maison

À ressortir le jour où la liste de causes à tenir à la main devient pénible,
en pratique autour de dix produits, ou si le volume de demandes augmente.

Ce qu'il apporterait, et que Ticket Tool ne peut pas faire :

- **Causes synchronisées** avec `public/products.json`, déjà généré à chaque
  publication par `scripts/annoncer_nouveaux_produits.py`. Un nouveau produit
  apparaîtrait tout seul dans le menu du ticket.
- Vérification du numéro de commande, statistiques, relances automatiques.

Ce qu'il coûte, et pourquoi il attend :

- Un bot qui répond à des clics doit être **en ligne en permanence**. Ce n'est
  pas un script lancé à la demande, c'est un service à héberger, surveiller et
  maintenir quand Discord fait évoluer son API.
- Tant que le gain est « ajouter une ligne dans un formulaire deux fois par
  an », le rapport est mauvais.

Le morceau difficile est déjà fait : `products.json` existe et se met à jour
tout seul. Le jour venu, il ne restera que le bot à écrire et à héberger.

---

## 10. Ce que je n'ai pas mis, et pourquoi
- **Pas de salon par produit.** Tu en as deux. Les balises du forum suffisent
  et évitent des salons déserts, qui donnent l'impression d'un produit mort.
- **Pas de vérification automatique des achats.** Fab ne fournit pas d'API
  publique pour ça aujourd'hui, à vérifier avant de promettre quoi que ce soit
  à tes clients.
