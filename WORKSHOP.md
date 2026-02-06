# 🎓 Workshop DevSecOps - 2 Jours

> **Problématique** : Comment apprendre les bonnes pratiques DevSecOps à l'heure de l'IA ?

## 📋 Informations pratiques

| Élément | Détail |
|---------|--------|
| **Durée** | 2 jours (14h) |
| **Public** | Étudiants, reconversions |
| **Niveau requis** | Bases WSL/Linux |
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
- [ ] Compte Cloud (un des suivants) :
  - Azure for Students : [azure.microsoft.com/free/students](https://azure.microsoft.com/free/students) ⭐
  - OU token Denv-r (fourni par formateur)

---

## 📅 Programme Jour 1 : Conteneurs & CI/CD

### Matin (9h - 12h30)

| Horaire | Module | Contenu |
|---------|--------|---------|
| 9h00 | ☕ **Accueil** | Présentation, tour de table |
| 9h30 | 📖 **Théorie** | [Histoire DevOps](./theory/01-devops-histoire.md) |
| 10h15 | ☕ **Pause** | |
| 10h30 | 📖 **Théorie** | Introduction Docker |
| 11h00 | 🎯 **Exercice** | [01 - Docker Basics](./exercises/jour-1/01-docker-basics.md) |
| 11h45 | 🎯 **Exercice** | [02 - Analyse Dockerfile](./exercises/jour-1/02-dockerfile-analysis.md) |

### Après-midi (14h - 17h30)

| Horaire | Module | Contenu |
|---------|--------|---------|
| 14h00 | 🎯 **Exercice** | [03 - Docker Debug](./exercises/jour-1/03-docker-debug.md) |
| 15h00 | ☕ **Pause** | |
| 15h15 | 📖 **Théorie** | Introduction CI/CD, GitHub Actions |
| 15h45 | 🎯 **Exercice** | [04 - GitHub Actions](./exercises/jour-1/04-github-actions.md) |
| 16h45 | 🤖 **Discussion** | IA et DevOps : limites et bon usage |
| 17h15 | 📝 **Debrief** | Q&A, preview Jour 2 |

---

## 📅 Programme Jour 2 : Cloud & Sécurité

### Matin (9h - 12h30)

| Horaire | Module | Contenu |
|---------|--------|---------|
| 9h00 | 📖 **Théorie** | [Cloud Fondamentaux](./theory/02-cloud-fondamentaux.md) |
| 9h45 | 📖 **Théorie** | [Comparatif Cloud](./theory/04-comparatif-cloud.md) |
| 10h15 | ☕ **Pause** | |
| 10h30 | 🎯 **Exercice** | [05 - Cloud Setup](./exercises/jour-2/05-cloud-setup.md) |
| 11h15 | 📖 **Théorie** | Introduction Terraform (IaC) |
| 11h45 | 🎯 **Exercice** | [06 - Terraform Basics](./exercises/jour-2/06-terraform-basics.md) |

### Après-midi (14h - 17h30)

| Horaire | Module | Contenu |
|---------|--------|---------|
| 14h00 | 📖 **Théorie** | Introduction Ansible |
| 14h30 | 🎯 **Exercice** | [07 - Ansible Playbook](./exercises/jour-2/07-ansible-playbook.md) |
| 15h15 | ☕ **Pause** | |
| 15h30 | 📖 **Théorie** | [GitOps](./theory/03-gitops-evolution.md) + DevSecOps |
| 16h00 | 🎯 **Exercice** | [08 - Security Scan](./exercises/jour-2/08-security-scan.md) |
| 16h45 | 🎯 **Capstone** | [09 - Full Deployment](./exercises/jour-2/09-full-deployment.md) |
| 17h15 | 📝 **Clôture** | Retour d'expérience, ressources pour aller plus loin |

---

## 📚 Ressources

### Théorie
- [01 - Histoire DevOps](./theory/01-devops-histoire.md)
- [02 - Cloud Fondamentaux](./theory/02-cloud-fondamentaux.md)
- [03 - GitOps](./theory/03-gitops-evolution.md)
- [04 - Comparatif Cloud](./theory/04-comparatif-cloud.md)

### Exercices
- [Index des exercices](./exercises/README.md)

### Troubleshooting
- [Erreurs courantes](./TROUBLESHOOTING.md)
- [Pièges IA](./AI_TRAPS.md)

---

## 🎯 Objectifs de la formation

À la fin des 2 jours, vous saurez :

### ✅ Jour 1
- [ ] Créer et exécuter des conteneurs Docker
- [ ] Lire et modifier un Dockerfile
- [ ] Comprendre un pipeline CI/CD GitHub Actions
- [ ] Debugger des erreurs de build

### ✅ Jour 2
- [ ] Créer des ressources cloud (VM, réseau)
- [ ] Utiliser Terraform pour l'Infrastructure as Code
- [ ] Exécuter des playbooks Ansible
- [ ] Scanner des vulnérabilités de sécurité

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
