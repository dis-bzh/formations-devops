# 🎯 Exercice 03 : Docker Debug

> 🟡 Niveau : Intermédiaire | ⏱️ Durée : 45 min

## Objectif

Apprendre à debugger des erreurs Docker courantes. Ce Dockerfile contient **volontairement des erreurs** à corriger.

## Prérequis

- Avoir fait les exercices 01 et 02
- Être dans le dossier du repo `denvr`

## Instructions

### Partie 1 : Le Dockerfile cassé (30 min)

1. **Créer un dossier de travail**
   ```bash
   mkdir ~/docker-debug && cd ~/docker-debug
   ```

2. **Créer un Dockerfile avec des erreurs**
   ```bash
   cat > Dockerfile << 'EOF'
   # Stage 1: deps
   FROM node:22-alpine AS deps
   WORKDIR /app
   COPY package.json ./
   RUN npm install
   
   # Stage 2: build
   FROM node:22-alpine AS builder
   WORKDIR /app
   COPY . .
   COPY --from=deps /app/nodes_modules ./node_modules
   RUN npm run build
   
   # Stage 3: production
   FROM nginx:stable-alpine-slim
   COPY --from=builder /app/out /usr/share/nginx/html
   EXPOSE 8080
   CMD ["nginx", "-g", "daemon off;"]
   EOF
   ```

3. **Créer les fichiers de l'app**
   ```bash
   cat > package.json << 'EOF'
   {
     "name": "debug-app",
     "scripts": {
       "build": "echo 'Building...' && mkdir -p out && echo '<h1>Debug Success</h1>' > out/index.html"
     }
   }
   EOF
   ```

4. **Essayer de builder**
   ```bash
   docker build -t debug-app:v1 .
   ```

   ❌ **Ça échoue !** Identifiez et corrigez les erreurs.

### Partie 2 : Les erreurs à trouver

Il y a **3 erreurs** dans ce Dockerfile. Trouvez-les !

| # | Type d'erreur | Indice |
|---|---------------|--------|
| 1 | Typo | Regardez attentivement les noms de dossiers |
| 2 | Fichier manquant | Que copie le stage 1 ? |
| 3 | Port incorrect | Quel port nginx utilise-t-il par défaut ? |

### Partie 3 : Techniques de debug (15 min)

1. **Lire les messages d'erreur attentivement**
   ```
   COPY failed: file not found in build context
   ```

2. **Builder jusqu'à un certain stage**
   ```bash
   docker build --target deps -t debug:deps .
   ```

3. **Inspecter un stage intermédiaire**
   ```bash
   docker run -it debug:deps sh
   ls -la
   ```

4. **Voir les layers de l'image**
   ```bash
   docker history debug-app:v1
   ```

---

## 🧪 Validation

✅ Vous avez réussi si :
- [ ] Le build passe sans erreur
- [ ] `docker run -d -p 8080:80 debug-app:v1` fonctionne
- [ ] http://localhost:8080 affiche "Debug Success"

---

## 💡 Indices progressifs

<details>
<summary>Indice 1 : Première erreur</summary>

Regardez la ligne :
```dockerfile
COPY --from=deps /app/nodes_modules ./node_modules
```
Comparez avec le nom réel du dossier créé par `npm install`.

</details>

<details>
<summary>Indice 2 : Deuxième erreur</summary>

Le stage `deps` copie `package.json`. Mais `npm install` a aussi besoin de `package-lock.json` s'il existe.

Plus important : créez un `package-lock.json` ou utilisez `package*.json` dans le COPY.

</details>

<details>
<summary>Indice 3 : Troisième erreur</summary>

`EXPOSE 8080` dans le Dockerfile, mais nginx écoute sur le port `80` par défaut.
L'expose ne change pas le port interne, seulement la documentation.

</details>

---

## ✅ Solution

<details>
<summary>Cliquer pour voir le Dockerfile corrigé</summary>

```dockerfile
# Stage 1: deps
FROM node:22-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm install

# Stage 2: build
FROM node:22-alpine AS builder
WORKDIR /app
COPY . .
COPY --from=deps /app/node_modules ./node_modules
RUN npm run build

# Stage 3: production
FROM nginx:stable-alpine-slim
COPY --from=builder /app/out /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

**Erreurs corrigées :**
1. `nodes_modules` → `node_modules` (typo)
2. `package.json` → `package*.json` (pour inclure le lock)
3. `EXPOSE 8080` → `EXPOSE 80` (port nginx par défaut)

</details>

---

## 🤖 Test IA

Copiez le Dockerfile cassé et demandez à une IA :

> *"Ce Dockerfile ne fonctionne pas, peux-tu le corriger ?"*

**Analysez :**
- L'IA trouve-t-elle les 3 erreurs ?
- Explique-t-elle *pourquoi* ce sont des erreurs ?
- Propose-t-elle des améliorations supplémentaires ?

**Leçon** : L'IA peut souvent repérer les typos, mais elle pourrait aussi "corriger" des choses qui ne sont pas cassées, ou manquer des erreurs subtiles.
