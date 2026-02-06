# 🎯 Exercice 02 : Analyse du Dockerfile

> 🟢 Niveau : Débutant | ⏱️ Durée : 30 min

## Objectif

Comprendre le Dockerfile du projet `denvr` et les bonnes pratiques appliquées.

## Prérequis

- Avoir fait l'exercice 01
- Être dans le dossier du repo `denvr`

## Instructions

### Partie 1 : Lire le Dockerfile (10 min)

1. **Ouvrir le Dockerfile du projet**
   ```bash
   cd ~/chemin/vers/denvr
   cat Dockerfile
   ```

2. **Répondre aux questions suivantes** (sans exécuter) :

   | Question | Votre réponse |
   |----------|---------------|
   | Combien y a-t-il de stages ? | |
   | Quelle est l'image de base du premier stage ? | |
   | Quel port est exposé ? | |
   | L'utilisateur final est-il root ? | |

### Partie 2 : Comprendre le multi-stage build (15 min)

Le Dockerfile utilise un **multi-stage build**. C'est une bonne pratique.

```dockerfile
# Stage 1: install dependencies
FROM node:22-alpine AS deps
WORKDIR /app
COPY my-app/package*.json ./
ARG NODE_ENV
ENV NODE_ENV $NODE_ENV
RUN npm install

# Stage 2: build
FROM node:22-alpine AS builder
WORKDIR /app
COPY ./my-app/ .
COPY --from=deps /app/node_modules ./node_modules
RUN npm run build

# Stage 3: production
FROM nginx:stable-alpine-slim
# ...
```

**Exercice** : Complétez le tableau

| Stage | Nom | But | Présent dans l'image finale ? |
|-------|-----|-----|-------------------------------|
| 1 | deps | Installer les dépendances npm | ❓ |
| 2 | builder | ❓ | ❓ |
| 3 | (final) | Servir l'application | ✅ |

### Partie 3 : Identifier les bonnes pratiques (5 min)

Cochez les bonnes pratiques présentes dans ce Dockerfile :

- [ ] **Multi-stage build** : Séparer build et runtime
- [ ] **Image alpine** : Images légères
- [ ] **User non-root** : Sécurité
- [ ] **COPY spécifique** : Pas de `COPY . .` global
- [ ] **.dockerignore** : Exclure fichiers inutiles
- [ ] **ARG/ENV** : Variables configurables

---

## 🧪 Validation

✅ Vous avez réussi si vous pouvez expliquer :
- [ ] Pourquoi on utilise 3 stages au lieu de 1
- [ ] Pourquoi `nginx` est utilisé plutôt que `node` pour le stage final
- [ ] Pourquoi on change d'utilisateur avec `USER nginx`

---

## 💡 Indice

**Pourquoi multi-stage ?**
- Stage 1+2 : Contiennent `node`, `npm`, les sources → **gros**
- Stage final : Contient seulement nginx + fichiers HTML → **petit**

Résultat : Image finale beaucoup plus légère et sécurisée.

---

## ✅ Solution

<details>
<summary>Cliquer pour voir les réponses</summary>

**Partie 1 - Questions :**

| Question | Réponse |
|----------|---------|
| Combien y a-t-il de stages ? | 3 |
| Image de base du premier stage ? | `node:22-alpine` |
| Port exposé ? | 80 |
| Utilisateur final root ? | Non, c'est `nginx` |

**Partie 2 - Tableau :**

| Stage | Nom | But | Présent dans l'image finale ? |
|-------|-----|-----|-------------------------------|
| 1 | deps | Installer les dépendances npm | ❌ |
| 2 | builder | Compiler l'application NextJS | ❌ |
| 3 | (final) | Servir l'application | ✅ |

**Partie 3 - Bonnes pratiques :**
- ✅ Multi-stage build
- ✅ Image alpine (légère)
- ✅ User non-root (`USER nginx`)
- ✅ COPY spécifique
- ✅ .dockerignore (vérifiez le fichier !)
- ✅ ARG/ENV pour NODE_ENV

</details>

---

## 🤖 Test IA

Demandez à une IA :

> *"Écris-moi un Dockerfile pour une application NextJS"*

**Comparez avec le Dockerfile du projet :**
- L'IA utilise-t-elle un multi-stage build ?
- L'utilisateur est-il root ou non-root ?
- L'image est-elle alpine ou une image lourde ?

**Leçon** : L'IA génère souvent un Dockerfile "qui marche" mais pas optimisé. Sans connaître les bonnes pratiques, vous ne pouvez pas évaluer sa réponse.
