# 🎯 Exercice 06 - Introduction au Monitoring

> **Objectif** : Découvrir les concepts de monitoring et observer des métriques

## 📋 Contexte

Le monitoring est essentiel pour comprendre ce qui se passe dans vos applications. Dans cet exercice, on va explorer les concepts de base et observer des logs en temps réel.

## 🎯 Mission

1. Comprendre les logs Docker
2. Observer des métriques de conteneur
3. Créer un healthcheck basique

---

## 📝 Instructions

### Étape 1 : Observer les logs Docker

```bash
# Lancer un conteneur nginx
docker run -d --name web nginx

# Voir les logs en temps réel
docker logs -f web

# Dans un autre terminal, générer du trafic
curl http://localhost:80  # (va échouer car pas de port mapping)

# Observer les logs
docker logs web
```

### Étape 2 : Ajouter le port mapping et observer

```bash
# Supprimer et recréer avec port mapping
docker rm -f web
docker run -d --name web -p 8080:80 nginx

# Générer du trafic
curl http://localhost:8080
curl http://localhost:8080/page-inexistante

# Observer les logs (succès et erreurs)
docker logs web
```

**Questions :**
- Comment différencier une requête réussie d'une erreur ?
- Quel format de log nginx utilise-t-il ?

### Étape 3 : Voir les métriques du conteneur

```bash
# Statistiques en temps réel
docker stats web

# CPU, mémoire, réseau, I/O
# Appuyez sur Ctrl+C pour quitter
```

### Étape 4 : Créer un healthcheck

Créez un fichier `Dockerfile.health` :

```dockerfile
FROM nginx:alpine

# Ajouter curl pour le healthcheck
RUN apk add --no-cache curl

# Définir un healthcheck
HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
  CMD curl -f http://localhost/ || exit 1

EXPOSE 80
```

Construisez et testez :

```bash
# Build
docker build -f Dockerfile.health -t nginx-health .

# Run
docker run -d --name web-health -p 8081:80 nginx-health

# Observer le status de santé
docker ps
# La colonne STATUS affichera "(healthy)" après quelques secondes

# Inspecter les healthchecks
docker inspect --format='{{json .State.Health}}' web-health | jq
```

### Étape 5 : Simuler un problème

```bash
# Entrer dans le conteneur
docker exec -it web-health sh

# Casser nginx (supprimer la page d'accueil)
rm /usr/share/nginx/html/index.html

# Sortir
exit

# Observer le changement de status
docker ps
# Le status passera à "(unhealthy)" après quelques checks
```

---

## ✅ Critères de succès

- [ ] Vous savez lire les logs Docker
- [ ] Vous comprenez `docker stats`
- [ ] Vous avez créé un healthcheck fonctionnel
- [ ] Vous avez observé le passage healthy → unhealthy

---

## 🔗 Lien avec le Capstone

Le monitoring sera crucial pour la "Secure AI Platform" :
- Healthchecks pour chaque service
- Logs centralisés
- Métriques de performance

---

## 📚 Ressources

- [Théorie : Monitoring et SRE](../../theory/06-monitoring-sre.md)
- [Docker Healthcheck](https://docs.docker.com/engine/reference/builder/#healthcheck)
- [Docker Stats](https://docs.docker.com/engine/reference/commandline/stats/)

---

## 🧹 Nettoyage

```bash
docker rm -f web web-health
docker rmi nginx-health
```
