# 🎯 Exercice 08 - Build et Push d'Images Docker

> **Objectif** : Créer une image Docker et la publier sur Docker Hub

## 📋 Contexte

Savoir créer et publier ses propres images est essentiel pour le déploiement d'applications conteneurisées.

## 🎯 Mission

1. Créer un Dockerfile optimisé
2. Builder l'image localement
3. Taguer et pusher sur Docker Hub

---

## 📝 Instructions

### Étape 1 : Créer l'application

Créez un dossier `my-api/` avec les fichiers suivants :

`my-api/app.py` :
```python
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from Secure AI Platform!",
        "version": os.getenv("APP_VERSION", "dev")
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

`my-api/requirements.txt` :
```
flask==3.0.0
gunicorn==21.2.0
```

### Étape 2 : Créer le Dockerfile

`my-api/Dockerfile` :
```dockerfile
# Étape 1 : Image de base légère
FROM python:3.11-slim

# Étape 2 : Métadonnées
LABEL maintainer="votre-email@example.com"
LABEL version="1.0"

# Étape 3 : Créer un utilisateur non-root (sécurité)
RUN useradd --create-home appuser
WORKDIR /home/appuser

# Étape 4 : Installer les dépendances (cache efficace)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : Copier le code
COPY app.py .

# Étape 6 : Changer d'utilisateur
USER appuser

# Étape 7 : Variables d'environnement
ENV APP_VERSION=1.0.0

# Étape 8 : Exposer le port
EXPOSE 5000

# Étape 9 : Healthcheck
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:5000/health || exit 1

# Étape 10 : Commande de démarrage (production)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

### Étape 3 : Builder l'image

```bash
cd my-api

# Builder avec un tag
docker build -t my-api:1.0.0 .

# Vérifier
docker images | grep my-api

# Tester localement
docker run -d --name test-api -p 5000:5000 my-api:1.0.0

# Tester
curl http://localhost:5000
curl http://localhost:5000/health

# Voir les logs
docker logs test-api

# Nettoyer
docker rm -f test-api
```

### Étape 4 : Se connecter à Docker Hub

```bash
# Créer un compte sur https://hub.docker.com si pas déjà fait

# Se connecter
docker login
# Entrer username et password
```

### Étape 5 : Taguer et pusher

```bash
# Taguer avec votre username Docker Hub
docker tag my-api:1.0.0 <votre-username>/my-api:1.0.0
docker tag my-api:1.0.0 <votre-username>/my-api:latest

# Pusher
docker push <votre-username>/my-api:1.0.0
docker push <votre-username>/my-api:latest

# Vérifier sur https://hub.docker.com
```

### Étape 6 : Tester le pull depuis Docker Hub

```bash
# Supprimer les images locales
docker rmi my-api:1.0.0 <votre-username>/my-api:1.0.0 <votre-username>/my-api:latest

# Puller depuis Docker Hub
docker pull <votre-username>/my-api:latest

# Exécuter
docker run -d -p 5000:5000 <votre-username>/my-api:latest
curl http://localhost:5000
```

---

## ✅ Critères de succès

- [ ] Dockerfile créé avec bonnes pratiques (user non-root, healthcheck)
- [ ] Image buildée et testée localement
- [ ] Image pushée sur Docker Hub
- [ ] Image pullée et fonctionnelle depuis Docker Hub

---

## 🔗 Lien avec le Capstone

Cette image servira de base pour la "Secure AI Platform". On l'intégrera dans une stack Docker Compose avec d'autres services !

---

## 📚 Ressources

- [Théorie : Introduction aux Conteneurs](../../theory/07-containers-intro.md)
- [Docker Hub](https://hub.docker.com/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

---

## 🧹 Nettoyage

```bash
docker rm -f $(docker ps -aq)
docker rmi my-api:1.0.0
```
