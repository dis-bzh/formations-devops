# 🎯 Exercice 01 : Docker Basics

> 🟢 Niveau : Débutant | ⏱️ Durée : 45 min

## Objectif

Comprendre les bases de Docker : images, conteneurs, build, run.

## Prérequis

- Docker installé (`docker --version`)
- Terminal WSL ou Linux

## Instructions

### Partie 1 : Premiers pas (15 min)

1. **Vérifier l'installation Docker**
   ```bash
   docker --version
   docker info
   ```

2. **Lancer votre premier conteneur**
   ```bash
   docker run hello-world
   ```
   > Que s'est-il passé ? Docker a téléchargé une image et exécuté un conteneur.

3. **Explorer une image**
   ```bash
   # Lancer un conteneur Ubuntu interactif
   docker run -it ubuntu:22.04 bash
   
   # Dans le conteneur, explorez :
   cat /etc/os-release
   whoami
   ls /
   
   # Pour sortir :
   exit
   ```

4. **Lister les conteneurs et images**
   ```bash
   # Conteneurs actifs
   docker ps
   
   # Tous les conteneurs (y compris arrêtés)
   docker ps -a
   
   # Images téléchargées
   docker images
   ```

### Partie 2 : Créer votre propre image (20 min)

1. **Créer un dossier de travail**
   ```bash
   mkdir ~/docker-lab && cd ~/docker-lab
   ```

2. **Créer un Dockerfile simple**
   ```bash
   cat > Dockerfile << 'EOF'
   FROM nginx:alpine
   COPY index.html /usr/share/nginx/html/
   EXPOSE 80
   EOF
   ```

3. **Créer une page HTML**
   ```bash
   cat > index.html << 'EOF'
   <!DOCTYPE html>
   <html>
   <head><title>Mon premier conteneur</title></head>
   <body>
     <h1>🐳 Bravo !</h1>
     <p>Vous avez créé votre premier conteneur Docker.</p>
   </body>
   </html>
   EOF
   ```

4. **Construire l'image**
   ```bash
   docker build -t mon-site:v1 .
   ```
   > L'option `-t` permet de "taguer" (nommer) l'image.

5. **Lancer le conteneur**
   ```bash
   docker run -d -p 8080:80 --name mon-site mon-site:v1
   ```
   > - `-d` : détaché (en arrière-plan)
   > - `-p 8080:80` : mapper le port 8080 local vers le port 80 du conteneur
   > - `--name` : donner un nom au conteneur

6. **Tester**
   ```bash
   curl http://localhost:8080
   # Ou ouvrir http://localhost:8080 dans un navigateur
   ```

### Partie 3 : Nettoyage (10 min)

1. **Arrêter le conteneur**
   ```bash
   docker stop mon-site
   ```

2. **Supprimer le conteneur**
   ```bash
   docker rm mon-site
   ```

3. **Supprimer l'image (optionnel)**
   ```bash
   docker rmi mon-site:v1
   ```

4. **Nettoyer tout (conteneurs arrêtés, images non utilisées)**
   ```bash
   docker system prune -a
   # ⚠️ Attention : supprime TOUT ce qui n'est pas utilisé !
   ```

---

## 🧪 Validation

✅ Vous avez réussi si :
- [ ] `docker run hello-world` affiche un message de succès
- [ ] Vous avez pu entrer dans un conteneur Ubuntu
- [ ] Votre site personnalisé s'affiche sur http://localhost:8080
- [ ] Vous savez lister et nettoyer les conteneurs/images

---

## 💡 Indice

Si le build échoue, vérifiez :
- Que vous êtes bien dans le dossier contenant le Dockerfile
- Que le fichier `index.html` existe
- Les messages d'erreur dans la sortie

---

## ✅ Solution

<details>
<summary>Cliquer pour voir les commandes complètes</summary>

```bash
# Tout en une fois
mkdir ~/docker-lab && cd ~/docker-lab

cat > Dockerfile << 'EOF'
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
EXPOSE 80
EOF

cat > index.html << 'EOF'
<!DOCTYPE html>
<html>
<head><title>Mon premier conteneur</title></head>
<body><h1>🐳 Bravo !</h1></body>
</html>
EOF

docker build -t mon-site:v1 .
docker run -d -p 8080:80 --name mon-site mon-site:v1
curl http://localhost:8080
```

</details>

---

## 🤖 Test IA

Essayez de poser cette question à une IA :

> *"J'ai lancé `docker run nginx` mais je ne peux pas accéder au site. Pourquoi ?"*

**Analysez la réponse :**
- L'IA mentionne-t-elle le mapping de ports (`-p`) ?
- Propose-t-elle de vérifier si le conteneur tourne (`docker ps`) ?
- La réponse est-elle adaptée à votre contexte (WSL, Linux...) ?

**Leçon** : L'IA donnera une réponse générique. Elle ne sait pas que vous avez oublié `-p 8080:80` si vous ne le mentionnez pas.
