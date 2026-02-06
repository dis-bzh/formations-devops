# 🎯 Exercice 05 : Cloud Setup

> 🟢 Niveau : Débutant | ⏱️ Durée : 45 min

## Objectif

Créer votre premier compte cloud et provisionner une VM.

## Prérequis

- Email éducation (.edu, .ac.fr...) OU token Denv-r fourni
- Navigateur web

## Instructions

Choisissez **UNE** des options suivantes :

---

## Option A : Azure for Students ⭐ (Recommandé)

### Étape 1 : Créer le compte (10 min)

1. Aller sur [azure.microsoft.com/free/students](https://azure.microsoft.com/free/students)
2. Cliquer "Démarrer gratuitement"
3. Se connecter avec votre email éducation
4. Vérifier votre statut étudiant

> [!NOTE]
> Pas de carte bancaire requise !

### Étape 2 : Créer une VM (20 min)

**Via le portail (interface web) :**

1. Aller sur [portal.azure.com](https://portal.azure.com)
2. Cliquer "Créer une ressource"
3. Chercher "Machine virtuelle"
4. Configurer :

   | Paramètre | Valeur |
   |-----------|--------|
   | Groupe de ressources | `formation-rg` (créer nouveau) |
   | Nom de la VM | `formation-vm` |
   | Région | `West Europe` |
   | Image | `Ubuntu Server 22.04 LTS` |
   | Taille | `Standard_B1s` (1 vCPU, 1 Go) |
   | Authentification | Clé SSH publique |

5. Générer une paire de clés SSH (télécharger la clé privée !)
6. Vérifier et créer

**Via Azure CLI (optionnel) :**

```bash
# Installer Azure CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Se connecter
az login

# Créer le groupe de ressources
az group create --name formation-rg --location westeurope

# Créer la VM
az vm create \
  --resource-group formation-rg \
  --name formation-vm \
  --image Ubuntu2204 \
  --size Standard_B1s \
  --admin-username azureuser \
  --generate-ssh-keys
```

### Étape 3 : Se connecter (10 min)

```bash
# Récupérer l'IP publique
az vm show -d -g formation-rg -n formation-vm --query publicIps -o tsv

# Se connecter
ssh -i ~/.ssh/id_rsa azureuser@<IP_PUBLIQUE>
```

### Étape 4 : Nettoyage

⚠️ **Important** : Supprimer les ressources après l'exercice !

```bash
az group delete --name formation-rg --yes --no-wait
```

---

## Option B : Denv-r (Token fourni)

### Étape 1 : Configurer le token (5 min)

```bash
# Token fourni par le formateur
export DENVR_API_TOKEN="votre-token-ici"

# Vérifier
curl -H "apikey: $DENVR_API_TOKEN" https://api.denv-r.com/v1/compute/virtual-machines
```

### Étape 2 : Créer une VM via l'API (20 min)

Voir le dossier `terraform/` du repo pour utiliser Terraform avec Denv-r.

---

## Option C : GCP Free Tier

### Étape 1 : Créer le compte (10 min)

1. Aller sur [cloud.google.com/free](https://cloud.google.com/free)
2. Se connecter avec compte Google
3. ⚠️ Carte bancaire requise (ne sera pas débitée)
4. Activer les $300 de crédits

### Étape 2 : Créer une VM (20 min)

```bash
# Installer gcloud
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init

# Créer la VM
gcloud compute instances create formation-vm \
  --zone=europe-west1-b \
  --machine-type=e2-micro \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud
```

### Étape 3 : Se connecter

```bash
gcloud compute ssh formation-vm --zone=europe-west1-b
```

### Étape 4 : Nettoyage

```bash
gcloud compute instances delete formation-vm --zone=europe-west1-b
```

---

## 🧪 Validation

✅ Vous avez réussi si :
- [ ] Vous avez un compte cloud actif
- [ ] Une VM est en cours d'exécution
- [ ] Vous pouvez vous y connecter en SSH
- [ ] Vous avez nettoyé après l'exercice

---

## 💡 Indice

Si la connexion SSH échoue :
1. Vérifiez que la VM est bien démarrée
2. Vérifiez les règles de firewall (port 22 ouvert)
3. Vérifiez que vous utilisez la bonne clé privée

---

## 🤖 Test IA

Demandez à une IA :

> *"Comment créer une VM Ubuntu sur Azure gratuitement ?"*

**Vérifiez :**
- L'IA mentionne-t-elle Azure for Students ?
- Les tailles de VM suggérées sont-elles dans le free tier ?
- L'IA précise-t-elle de nettoyer les ressources après ?

**Leçon** : L'IA peut donner des commandes correctes mais ne connaît pas les limites de votre compte gratuit.
