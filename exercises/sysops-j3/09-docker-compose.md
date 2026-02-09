# 🎯 Exercice 09 - Docker Compose

> **Objectif** : Orchestrer plusieurs conteneurs avec Docker Compose

## 📋 Contexte

Une application moderne est rarement un seul conteneur. On va apprendre à orchestrer plusieurs services ensemble.

## 🎯 Mission

Créer une stack Docker Compose avec :
1. Une application Python (API)
2. Une base de données Redis
3. Un réseau privé entre les deux

## 📝 Instructions

### Étape 1 : Créer l'application

Créez `app/main.py` :

```python
from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)
cache = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return jsonify({
        "message": "Hello from Secure AI Platform!",
        "visits": int(count)
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Créez `app/requirements.txt` :

```
flask==3.0.0
redis==5.0.0
```

Créez `app/Dockerfile` :

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
EXPOSE 5000
CMD ["python", "main.py"]
```

### Étape 2 : Créer le docker-compose.yml

```yaml
services:
  app:
    build: ./app
    ports:
      - "5000:5000"
    environment:
      - REDIS_HOST=redis
    depends_on:
      - redis
    networks:
      - backend

  redis:
    image: redis:alpine
    networks:
      - backend

networks:
  backend:
    driver: bridge
```

### Étape 3 : Lancer et tester

```bash
# Lancer la stack
docker compose up -d

# Vérifier les logs
docker compose logs -f

# Tester
curl http://localhost:5000
curl http://localhost:5000
curl http://localhost:5000

# Arrêter
docker compose down
```

## ✅ Critères de succès

- [ ] Les deux conteneurs démarrent
- [ ] Le compteur de visites s'incrémente
- [ ] Vous comprenez le rôle du réseau `backend`

## 🔗 Lien avec le Capstone

On ajoutera bientôt **Presidio** (anonymisation) comme 3ème service dans cette stack !

## 📚 Ressources

- [Docker Compose documentation](https://docs.docker.com/compose/)
- [Compose file reference](https://docs.docker.com/compose/compose-file/)
