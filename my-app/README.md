# 🚀 my-app — Application Hello World

Application Next.js simple servant de base pour le workshop DevSecOps.

## 📋 Objectif pédagogique

Cette application "Hello World" est utilisée pour :
1. **J1** — Premier workflow CI/CD (build, test, lint)
2. **J2** — Déploiement sur VM denv-r
3. **J3** — Containerisation avec Docker
4. **J4** — Évolution vers le capstone (Plateforme IA Sécurisée)

## 🛠️ Stack technique

| Technologie | Version |
|-------------|---------|
| Next.js | 15.1.6 |
| React | 19.0.0 |
| TypeScript | 5.x |
| TailwindCSS | 3.4.1 |

## 🚀 Démarrage rapide

```bash
# Installation
cd my-app
npm install

# Développement
npm run dev
# → http://localhost:3000

# Build production
npm run build
npm start

# Lint
npm run lint
```

## 🐳 Docker

```bash
# Build l'image
docker build -t my-app .

# Lancer le conteneur
docker run -p 3000:3000 my-app
```

## 📁 Structure

```
my-app/
├── app/           # Pages Next.js (App Router)
│   ├── page.tsx   # Page principale
│   └── layout.tsx # Layout global
├── public/        # Assets statiques
├── package.json   # Dépendances
└── Dockerfile     # Image Docker (à créer en exercice)
```

## ➡️ Prochaine étape

Après cette application simple, passez au **Capstone** dans `../capstone/` pour déployer une plateforme IA sécurisée complète.
