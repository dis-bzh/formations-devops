# 🤖 AI Traps - Quand l'IA se trompe

> Exercices démontrant les limites de l'IA et l'importance de la compréhension humaine.

## 🎯 Objectif

Ces "pièges" montrent des cas où demander directement à l'IA produit des réponses incorrectes ou dangereuses. L'objectif est de développer votre sens critique.

---

## Piège 1 : Le contexte manquant

### Situation
Vous demandez à l'IA :
> *"Comment installer Docker ?"*

### Problème avec la réponse IA
L'IA donnera probablement :
```bash
sudo apt install docker.io
```

### Ce qui manque
- Êtes-vous sur Ubuntu, Debian, CentOS, macOS ?
- Voulez-vous Docker Engine ou Docker Desktop ?
- Sur WSL2, les instructions sont différentes

### Leçon
**Toujours préciser le contexte** : OS, version, environnement.

---

## Piège 2 : Le code "qui marche" mais mal

### Situation
Vous demandez :
> *"Écris un Dockerfile pour mon app Node.js"*

### Réponse IA typique
```dockerfile
FROM node:latest
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 3000
CMD ["npm", "start"]
```

### Problèmes non détectés
1. `node:latest` → Non reproductible (version aléatoire)
2. `COPY . .` → Copie les node_modules, le .git, tout
3. Pas de multi-stage → Image lourde
4. Utilisateur root → Risque sécurité
5. Pas de .dockerignore mentionné

### Version correcte
```dockerfile
FROM node:22-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

FROM node:22-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
USER node
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### Leçon
**L'IA génère du code fonctionnel, pas optimal.** Sans connaître les bonnes pratiques, vous ne pouvez pas évaluer sa réponse.

---

## Piège 3 : Les credentials en clair

### Situation
> *"Comment se connecter à une base de données MySQL avec Node.js ?"*

### Réponse IA dangereuse
```javascript
const mysql = require('mysql');
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'motdepasse123',
  database: 'mydb'
});
```

### Problèmes
- Mot de passe en dur dans le code
- Sera commité dans Git → Fuite de secrets
- Utilisation de root → Mauvaise pratique

### Version sécurisée
```javascript
const mysql = require('mysql');
const connection = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME
});
```

### Leçon
**L'IA ne pense pas à la sécurité par défaut.** Toujours vérifier la gestion des secrets.

---

## Piège 4 : Les versions obsolètes

### Situation
> *"Comment configurer un workflow GitHub Actions pour déployer sur Kubernetes ?"*

### Problème
L'IA a été entraînée sur des données anciennes. Elle peut suggérer :
- Des actions `@v1` alors que `@v4` existe
- Des syntaxes dépréciées
- Des images Docker obsolètes

### Vérifications
1. Consulter la documentation officielle (toujours à jour)
2. Vérifier la date des exemples trouvés
3. Tester dans un environnement isolé

### Leçon
**L'IA n'est pas à jour.** Vérifiez toujours les versions et la documentation officielle.

---

## Piège 5 : L'hallucination de commandes

### Situation
> *"Comment lister les pods Kubernetes avec leur consommation mémoire ?"*

### Réponse IA potentiellement fausse
```bash
kubectl get pods --show-memory  # Cette option N'EXISTE PAS
```

### Réponse correcte
```bash
kubectl top pods
```

### Leçon
**L'IA peut inventer des options qui n'existent pas.** Toujours vérifier avec `--help` ou la doc officielle.

---

## Exercice : Testez vous-même

Posez ces questions à une IA et analysez les réponses :

| Question | Points à vérifier |
|----------|-------------------|
| "Comment sécuriser un serveur Linux ?" | Mentionne-t-elle fail2ban, UFW, les updates ? |
| "Écris un terraform pour créer une VM Azure" | Le code gère-t-il le réseau, les security groups ? |
| "Comment corriger une erreur 'permission denied' Docker ?" | Suggère-t-elle sudo (quick fix) ou usermod (bonne pratique) ? |

---

## 📊 Statistique importante

> **70% des développeurs** utilisent l'IA pour coder (2025)
> Mais **seulement 30%** vérifient systématiquement les réponses.

Source : Stack Overflow Developer Survey

---

## ✅ Bonnes pratiques avec l'IA

1. **Précisez le contexte** : OS, versions, contraintes
2. **Demandez les sources** : "Où puis-je vérifier cette information ?"
3. **Testez dans un environnement isolé** : Jamais directement en prod
4. **Vérifiez les versions** : L'IA peut être obsolète
5. **Ne copiez jamais aveuglément** : Comprenez ce que vous exécutez
6. **Utilisez l'IA comme assistant, pas comme autorité**
