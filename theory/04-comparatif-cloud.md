# 🌐 Comparatif Cloud & Crédits Gratuits

> Comment choisir son cloud et obtenir des crédits pour apprendre ?

## 🎯 Objectifs pédagogiques
- Comparer les principaux cloud providers
- Connaître les programmes de crédits gratuits
- Choisir le bon cloud pour vos besoins

---

## 🏢 Les "Big 3" + Alternatives

### Comparatif général

| Provider | Part de marché (2025) | Forces | Faiblesses |
|----------|----------------------|--------|------------|
| **AWS** | ~32% | Complet, mature, communauté | Complexe, pricing opaque |
| **Azure** | ~23% | Intégration Microsoft, enterprise | Naming confus |
| **GCP** | ~11% | Data/ML, Kubernetes (GKE) | Moins de services |
| **Denv-r** | Niche | Simple, français, GPU | Moins de services |

### Services équivalents

| Besoin | AWS | Azure | GCP | Denv-r |
|--------|-----|-------|-----|--------|
| **VM** | EC2 | Virtual Machines | Compute Engine | Warren VM |
| **Stockage objet** | S3 | Blob Storage | Cloud Storage | S3-compatible |
| **Kubernetes** | EKS | AKS | GKE | - |
| **Serverless** | Lambda | Functions | Cloud Functions | - |
| **Base de données** | RDS | SQL Database | Cloud SQL | - |

---

## 🎓 Programmes Crédits Étudiants

### Azure for Students ⭐ Recommandé

| Aspect | Détail |
|--------|--------|
| **Crédits** | **$100/an** |
| **Durée** | 12 mois, renouvelable |
| **Carte bancaire** | ❌ Non requise |
| **Condition** | Adresse email éducation (.edu, .ac.fr...) |
| **Lien** | [azure.microsoft.com/free/students](https://azure.microsoft.com/free/students) |

**Services inclus (gratuits) :**
- Azure App Service (hébergement web)
- Azure Cosmos DB (25 GB)
- Azure DevOps (5 utilisateurs)
- Visual Studio Code extensions

> [!TIP]
> **Recommandé pour cette formation** car :
> - Pas de CB requise = pas de risque de facturation
> - Interface en français disponible
> - Suffisant pour tous les exercices

### AWS Educate

| Aspect | Détail |
|--------|--------|
| **Crédits** | Variables selon programme |
| **Durée** | Variable |
| **Conditions** | Email éducation + validation |
| **Lien** | [aws.amazon.com/education/awseducate](https://aws.amazon.com/education/awseducate) |

**Inclus :**
- Labs pratiques gratuits
- Formations en ligne
- Parcours certifications

### Google Cloud Free Tier

| Aspect | Détail |
|--------|--------|
| **Crédits** | **$300 pendant 90 jours** |
| **Carte bancaire** | ✅ Requise (pas débitée) |
| **Lien** | [cloud.google.com/free](https://cloud.google.com/free) |

**Services "Always Free" :**
- 1 VM e2-micro (US regions)
- 5 GB Cloud Storage
- BigQuery (1 TB/mois)

### Denv-r (fourni par le formateur)

| Aspect | Détail |
|--------|--------|
| **Crédits** | Tokens API fournis |
| **Configuration** | Simple, API unique |
| **Avantage** | Terraform Warren provider |

---

## 🚀 Setup rapide par plateforme

### Option A : Azure (Recommandé)

```bash
# 1. Créer compte Azure for Students
# → Aller sur https://azure.microsoft.com/free/students
# → Se connecter avec email éducation

# 2. Installer Azure CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# 3. Se connecter
az login

# 4. Créer un groupe de ressources
az group create --name formation-rg --location westeurope

# 5. Créer une VM
az vm create \
  --resource-group formation-rg \
  --name formation-vm \
  --image Ubuntu2204 \
  --admin-username azureuser \
  --generate-ssh-keys
```

### Option B : Denv-r (Tokens fournis)

```bash
# 1. Récupérer votre token API (fourni par formateur)
export DENVR_API_TOKEN="votre-token"

# 2. Utiliser Terraform (voir ./terraform/)
cd terraform
terraform init -backend-config=backend.tfvars
terraform plan
terraform apply
```

### Option C : GCP (CB requise)

```bash
# 1. Créer compte Google Cloud
# → Aller sur https://cloud.google.com/free

# 2. Installer gcloud CLI
curl https://sdk.cloud.google.com | bash

# 3. Initialiser
gcloud init

# 4. Créer une VM
gcloud compute instances create formation-vm \
  --zone=europe-west1-b \
  --machine-type=e2-micro \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud
```

---

## ⚠️ Pièges à éviter

> [!WARNING]
> **Éviter les surprises de facturation :**

| Piège | Solution |
|-------|----------|
| Oublier des VMs allumées | Configurer des alertes budget |
| Trafic réseau sortant | Surveiller les coûts egress |
| Disques non supprimés | Nettoyer après chaque lab |
| Upgrade accidentel | Utiliser les tailles minimales |

### Commandes de nettoyage

```bash
# Azure : supprimer le groupe de ressources (tout dedans)
az group delete --name formation-rg --yes

# GCP : supprimer la VM
gcloud compute instances delete formation-vm --zone=europe-west1-b

# Denv-r : Terraform
terraform destroy
```

---

## 📊 Quel cloud choisir ?

```
┌─────────────────────────────────────────────────────────────────┐
│                    Arbre de décision                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Avez-vous un email éducation ?                                 │
│       │                                                         │
│       ├── OUI ──► Azure for Students ($100, pas de CB)          │
│       │                                                         │
│       └── NON ──► Le formateur fournit-il des tokens ?          │
│                        │                                        │
│                        ├── OUI ──► Denv-r                       │
│                        │                                        │
│                        └── NON ──► GCP Free ($300, CB requise)  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📚 Sources officielles

| Ressource | Lien |
|-----------|------|
| Azure for Students | [azure.microsoft.com/free/students](https://azure.microsoft.com/free/students) |
| AWS Educate | [aws.amazon.com/education/awseducate](https://aws.amazon.com/education/awseducate) |
| GCP Free Tier | [cloud.google.com/free](https://cloud.google.com/free) |
| Denv-r API | [api.denv-r.com](https://api.denv-r.com) |

---

## 🤔 Questions de réflexion

1. Pourquoi les cloud providers offrent-ils des crédits gratuits aux étudiants ?
2. Quels sont les risques du "vendor lock-in" ?
3. Comment choisiriez-vous un cloud pour un projet professionnel ?
