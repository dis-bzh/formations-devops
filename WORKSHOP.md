# 🎓 Formation DevSecOps - 4 Jours

> **Fil rouge** : Construire une "Secure AI Platform" — déployer une application IA sécurisée de A à Z.

## 📋 Informations pratiques

| Élément | Détail |
|---------|--------|
| **Durée** | 4 jours (2x2 jours, 28h total) |
| **Modules** | INFAL198 DevOps (J1-J2) + INFAL122 SysOps (J3-J4) |
| **Public** | Étudiants, reconversions |
| **Niveau requis** | Bases réseau (IP, DNS), Linux (commandes de base), Git |
| **Matériel** | PC avec WSL2, Docker Desktop |

---

## 🛠️ Prérequis techniques

### À installer avant la formation

```bash
# Windows : Activer WSL2
wsl --install

# Dans WSL (Ubuntu)
sudo apt update && sudo apt upgrade -y
sudo apt install -y git curl wget

# Docker Desktop (Windows)
# → Télécharger sur https://docker.com/products/docker-desktop

# Vérifications
docker --version
git --version
```

### Comptes à créer

- [ ] Compte GitHub : [github.com/signup](https://github.com/signup)
- [ ] Compte Docker Hub : [hub.docker.com](https://hub.docker.com)
- [ ] Compte Cloud : Token Denv-r (fourni par formateur)

---

## 📅 Module 1 : DevOps (INFAL198) — Jours 1-2

### Jour 1 : Culture DevOps & CI/CD

#### Matin (9h - 12h30)

| Horaire | Module | Contenu |
|---------|--------|---------|
| 9h00 | ☕ **Accueil** | Présentation, tour de table, objectifs |
| 9h30 | 📖 **Théorie** | [Histoire DevOps](./theory/01-devops-histoire.md) |
| 10h15 | ☕ **Pause** | |
| 10h30 | 📖 **Théorie** | [Introduction CI/CD](./theory/05-cicd-introduction.md) |
| 11h15 | 🎯 **Exercice** | [01 - Découverte DevOps](./exercises/devops-j1/01-devops-decouverte.md) |

#### Après-midi (14h - 17h30)

| Horaire | Module | Contenu |
|---------|--------|---------|
| 14h00 | 🎯 **Exercice** | [02 - Premier Workflow](./exercises/devops-j1/02-premier-workflow.md) |
| 15h00 | ☕ **Pause** | |
| 15h15 | 🎯 **Exercice** | [03 - Build & Test](./exercises/devops-j1/03-build-test.md) |
| 16h30 | 🤖 **Discussion** | IA et DevOps : limites et bon usage |
| 17h15 | 📝 **Debrief** | Q&A, preview Jour 2 |

**🔨 Capstone J1** : Créer le repo Git de la Secure AI Platform + premier workflow CI

---

### Jour 2 : Cloud & IaC

#### Matin (9h - 12h30)

| Horaire | Module | Contenu |
|---------|--------|---------|
| 9h00 | 📖 **Théorie** | [Cloud Fondamentaux](./theory/02-cloud-fondamentaux.md) |
| 9h45 | 📖 **Théorie** | [Comparatif Cloud](./theory/04-comparatif-cloud.md) |
| 10h15 | ☕ **Pause** | |
| 10h30 | 🎯 **Exercice** | [04 - Cloud Setup](./exercises/devops-j2/04-cloud-setup.md) |
| 11h15 | 🎯 **Exercice** | [05 - Terraform Basics](./exercises/devops-j2/05-terraform-basics.md) |

#### Après-midi (14h - 17h30)

| Horaire | Module | Contenu |
|---------|--------|---------|
| 14h00 | 📖 **Théorie** | [Monitoring & SRE](./theory/06-monitoring-sre.md) |
| 14h45 | 🎯 **Exercice** | [06 - Monitoring Intro](./exercises/devops-j2/06-monitoring-intro.md) |
| 15h30 | ☕ **Pause** | |
| 15h45 | 📝 **Synthèse** | Récap Module DevOps, preview SysOps |

**🔨 Capstone J2** : Infra Terraform VM + observer les logs

---

## 📅 Module 2 : SysOps (INFAL122) — Jours 3-4

### Jour 3 : Containers & Orchestration

#### Matin (9h - 12h30)

| Horaire | Module | Contenu |
|---------|--------|---------|
| 9h00 | 📖 **Théorie** | [Introduction Containers](./theory/07-containers-intro.md) |
| 9h45 | 🎯 **Exercice** | [07 - Docker Basics](./exercises/sysops-j3/07-docker-basics.md) |
| 10h30 | ☕ **Pause** | |
| 10h45 | 🎯 **Exercice** | [08 - Dockerfile Build](./exercises/sysops-j3/08-dockerfile-build.md) |
| 11h30 | 🎯 **Exercice** | [09 - Docker Compose](./exercises/sysops-j3/09-docker-compose.md) |

#### Après-midi (14h - 17h30)

| Horaire | Module | Contenu |
|---------|--------|---------|
| 14h00 | 📖 **Théorie** | [Introduction Kubernetes](./theory/08-kubernetes-intro.md) |
| 14h45 | 🎯 **Démo** | [10 - Kubernetes Demo](./exercises/sysops-j3/10-kubernetes-demo.md) |
| 15h30 | ☕ **Pause** | |
| 15h45 | 📝 **Debrief** | Q&A, preview Jour 4 |

**🔨 Capstone J3** : Docker Compose multi-containers (app + Presidio)

---

### Jour 4 : Automatisation & Sécurité

#### Matin (9h - 12h30)

| Horaire | Module | Contenu |
|---------|--------|---------|
| 9h00 | 📖 **Théorie** | [GitOps & DevSecOps](./theory/03-gitops-evolution.md) |
| 9h45 | 🎯 **Exercice** | [11 - Ansible Playbook](./exercises/sysops-j4/11-ansible-playbook.md) |
| 10h30 | ☕ **Pause** | |
| 10h45 | 🎯 **Exercice** | [12 - Security Scan](./exercises/sysops-j4/12-security-scan.md) |

#### Après-midi (14h - 17h30)

| Horaire | Module | Contenu |
|---------|--------|---------|
| 14h00 | 🎯 **Capstone** | [13 - Secure AI Platform](./exercises/sysops-j4/13-capstone.md) |
| 16h30 | 🎤 **Démo** | Présentation des projets |
| 17h00 | 📝 **Clôture** | Retour d'expérience, ressources |

**🔨 Capstone Final** : Déploiement complet de la Secure AI Platform

---

## 📚 Ressources

### Théorie
| # | Module | Jour |
|---|--------|------|
| 01 | [Histoire DevOps](./theory/01-devops-histoire.md) | J1 |
| 02 | [Cloud Fondamentaux](./theory/02-cloud-fondamentaux.md) | J2 |
| 03 | [GitOps & DevSecOps](./theory/03-gitops-evolution.md) | J4 |
| 04 | [Comparatif Cloud](./theory/04-comparatif-cloud.md) | J2 |
| 05 | [Introduction CI/CD](./theory/05-cicd-introduction.md) | J1 |
| 06 | [Monitoring & SRE](./theory/06-monitoring-sre.md) | J2 |
| 07 | [Introduction Containers](./theory/07-containers-intro.md) | J3 |
| 08 | [Introduction Kubernetes](./theory/08-kubernetes-intro.md) | J3 |

### Exercices
- [Index des exercices](./exercises/README.md)

### Troubleshooting
- [Erreurs courantes](./TROUBLESHOOTING.md)
- [Pièges IA](./AI_TRAPS.md)

---

## 🎯 Objectifs de la formation

### ✅ Module DevOps (J1-J2)
- [ ] Comprendre la culture et les enjeux DevOps
- [ ] Créer un pipeline CI/CD avec GitHub Actions
- [ ] Provisionner une infrastructure avec Terraform
- [ ] Configurer du monitoring basique

### ✅ Module SysOps (J3-J4)
- [ ] Créer et publier des images Docker
- [ ] Orchestrer des conteneurs avec Docker Compose
- [ ] Comprendre l'architecture Kubernetes (théorie + démo)
- [ ] Automatiser avec Ansible
- [ ] Scanner et corriger des vulnérabilités

### 🧠 Compétences transverses
- [ ] Savoir quand faire confiance (ou non) à l'IA
- [ ] Lire de la documentation officielle
- [ ] Debugger par soi-même avant de demander de l'aide

---

## 💡 Philosophie de la formation

> [!IMPORTANT]
> **L'objectif n'est pas de tout mémoriser, mais de comprendre :**
> - *Pourquoi* ces outils existent
> - *Comment* chercher quand on ne sait pas
> - *Quand* l'IA peut aider vs quand elle nous induit en erreur
