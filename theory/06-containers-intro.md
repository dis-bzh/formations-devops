# 📦 Introduction aux Conteneurs

> *"Build once, run anywhere."*

## 🎯 Objectifs pédagogiques
- Comprendre l'origine et l'évolution de la conteneurisation
- Différencier conteneurs et machines virtuelles
- Connaître Docker et ses alternatives (Podman)

---

## 📅 Chronologie

### Avant les conteneurs : le problème

```
┌─────────────────────────────────────────────────────┐
│  Développeur                     Ops/Production     │
│  ┌─────────────┐                ┌─────────────┐     │
│  │  "Ça marche │                │  "Ça marche │     │
│  │  chez moi!" │      ≠         │  pas chez   │     │
│  │             │                │   nous!"    │     │
│  │  Python 3.9 │                │  Python 3.6 │     │
│  │  Ubuntu 22  │                │  RHEL 7     │     │
│  └─────────────┘                └─────────────┘     │
└─────────────────────────────────────────────────────┘
```

**Problèmes :**
- Différences d'environnement (versions, dépendances)
- "Dependency hell"
- Déploiements lents et risqués

### L'évolution

| Année | Technologie | Description |
|-------|-------------|-------------|
| 1979 | **chroot** | Isolation du filesystem Unix |
| 2000 | **FreeBSD Jails** | Isolation complète de processus |
| 2006 | **cgroups** | Google crée les Control Groups (Linux) |
| 2008 | **LXC** | Linux Containers, premier "conteneur" moderne |
| 2013 | **Docker** | Démocratise la conteneurisation |
| 2015 | **Kubernetes** | Orchestration de conteneurs à grande échelle |
| 2019 | **Podman** | Alternative rootless à Docker |

---

## 🔍 Conteneur vs Machine Virtuelle

```
┌─────────────────────────────────────────────────────────────────┐
│                    MACHINE VIRTUELLE                             │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐                            │
│  │  App A  │ │  App B  │ │  App C  │                            │
│  ├─────────┤ ├─────────┤ ├─────────┤                            │
│  │  Libs   │ │  Libs   │ │  Libs   │                            │
│  ├─────────┤ ├─────────┤ ├─────────┤                            │
│  │Guest OS │ │Guest OS │ │Guest OS │  ← OS complet par VM       │
│  └─────────┘ └─────────┘ └─────────┘                            │
│  ┌───────────────────────────────────┐                          │
│  │          HYPERVISOR               │                          │
│  └───────────────────────────────────┘                          │
│  ┌───────────────────────────────────┐                          │
│  │           HOST OS                 │                          │
│  └───────────────────────────────────┘                          │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                      CONTENEURS                                  │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐                            │
│  │  App A  │ │  App B  │ │  App C  │                            │
│  ├─────────┤ ├─────────┤ ├─────────┤                            │
│  │  Libs   │ │  Libs   │ │  Libs   │                            │
│  └─────────┘ └─────────┘ └─────────┘                            │
│  ┌───────────────────────────────────┐                          │
│  │      CONTAINER RUNTIME (Docker)   │  ← Pas d'OS invité      │
│  └───────────────────────────────────┘                          │
│  ┌───────────────────────────────────┐                          │
│  │           HOST OS (Linux)         │                          │
│  └───────────────────────────────────┘                          │
└─────────────────────────────────────────────────────────────────┘
```

### Comparaison

| Aspect | VM | Conteneur |
|--------|-----|-----------|
| **Taille** | Go (OS complet) | Mo (binaires + libs) |
| **Démarrage** | Minutes | Secondes |
| **Isolation** | Forte (hardware) | Modérée (kernel partagé) |
| **Performance** | Overhead hyperviseur | Quasi-native |
| **Portabilité** | Limitée | Excellente |

---

## 🐳 Docker : concepts clés

### Image vs Conteneur

| Concept | Analogie | Description |
|---------|----------|-------------|
| **Image** | Recette / Template | Fichier en lecture seule |
| **Conteneur** | Gâteau / Instance | Processus en cours d'exécution |
| **Registry** | Bibliothèque | Stockage et partage d'images |

### Architecture Docker

```
┌─────────────────────────────────────────────────────┐
│                    Docker Client                     │
│                  (docker build, run)                 │
└─────────────────────┬───────────────────────────────┘
                      │ REST API
┌─────────────────────▼───────────────────────────────┐
│                    Docker Daemon                     │
│                     (dockerd)                        │
├─────────────────────────────────────────────────────┤
│  Images    │    Containers    │    Networks         │
│  Registry  │    Volumes       │                     │
└─────────────────────────────────────────────────────┘
```

### Commandes essentielles

```bash
# Télécharger une image
docker pull python:3.11

# Lister les images
docker images

# Exécuter un conteneur
docker run -it python:3.11 bash

# Lister les conteneurs
docker ps -a

# Arrêter un conteneur
docker stop <container_id>

# Supprimer un conteneur
docker rm <container_id>
```

---

## 🦭 Podman : alternative à Docker

| Aspect | Docker | Podman |
|--------|--------|--------|
| **Daemon** | Oui (dockerd) | Non (daemonless) |
| **Root** | Requis par défaut | Rootless par défaut |
| **Compatibilité** | - | CLI compatible Docker |
| **Pods** | Non natif | Natif (comme K8s) |

```bash
# Podman utilise la même syntaxe que Docker
podman run -it python:3.11 bash

# Alias possible
alias docker=podman
```

> [!TIP]
> Pour cette formation, on utilise Docker (plus répandu), mais Podman est mentionné dans le programme INFAL122.

---

## ❓ Pourquoi c'est important en 2026 ?

> [!IMPORTANT]
> Les conteneurs sont **omniprésents** :
> - 80%+ des workloads cloud utilisent des conteneurs
> - Base de Kubernetes et des architectures cloud-native
> - Compétence requise pour tous les rôles DevOps/SysOps

---

## 📚 Sources officielles

| Ressource | Lien |
|-----------|------|
| Docker Documentation | [docs.docker.com](https://docs.docker.com/) |
| Podman Documentation | [podman.io/docs](https://podman.io/docs/) |
| OCI (Open Container Initiative) | [opencontainers.org](https://opencontainers.org/) |
| Docker Hub | [hub.docker.com](https://hub.docker.com/) |

---

## 🤔 Questions de réflexion

1. Pourquoi Docker a-t-il "gagné" face à LXC ?
2. Quand préférer une VM à un conteneur ?
3. Quels sont les risques de sécurité des conteneurs ?
