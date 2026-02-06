# 🎯 Exercice 06 : Terraform Basics

> 🟡 Niveau : Intermédiaire | ⏱️ Durée : 45 min

## Objectif

Découvrir l'Infrastructure as Code (IaC) avec Terraform.

## Prérequis

- Terraform installé
- Compte cloud configuré (exercice 05)

## Instructions

### Partie 1 : Comprendre Terraform (15 min)

**Qu'est-ce que Terraform ?**

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Fichiers .tf  │────►│    Terraform    │────►│  Infrastructure │
│   (déclaratif)  │     │   Plan/Apply    │     │     Cloud       │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

**Concepts clés :**

| Concept | Description | Exemple |
|---------|-------------|---------|
| **Provider** | Plugin cloud | `azurerm`, `aws`, `warren` |
| **Resource** | Objet à créer | VM, réseau, IP |
| **State** | État actuel | `terraform.tfstate` |
| **Plan** | Prévisualisation | Ce qui va changer |
| **Apply** | Exécution | Crée/modifie les ressources |

### Partie 2 : Analyser le code existant (15 min)

1. **Explorer le dossier Terraform du projet**
   ```bash
   cd terraform
   ls -la
   ```

2. **Lire les fichiers**

   | Fichier | Contenu |
   |---------|---------|
   | `provider.tf` | Configuration du provider cloud |
   | `variables.tf` | Variables d'entrée |
   | `main.tf` | Ressources à créer |
   | `output.tf` | Valeurs de sortie |
   | `*.tfvars.example` | Exemples de variables |

3. **Analyser `main.tf`**
   ```bash
   cat main.tf
   ```

   Identifiez :
   - [ ] Les ressources `warren_network`
   - [ ] Les ressources `warren_virtual_machine`
   - [ ] Les ressources `warren_floating_ip`

### Partie 3 : Premier projet Terraform (15 min)

Créons un exemple simple (sans cloud réel) :

1. **Créer un dossier**
   ```bash
   mkdir ~/tf-lab && cd ~/tf-lab
   ```

2. **Créer `main.tf`**
   ```hcl
   # Fichier: main.tf
   
   # Provider local (pas besoin de cloud)
   terraform {
     required_providers {
       local = {
         source  = "hashicorp/local"
         version = "~> 2.0"
       }
     }
   }
   
   # Variable
   variable "message" {
     default = "Hello from Terraform!"
   }
   
   # Ressource : créer un fichier
   resource "local_file" "hello" {
     content  = var.message
     filename = "${path.module}/hello.txt"
   }
   
   # Output
   output "file_path" {
     value = local_file.hello.filename
   }
   ```

3. **Exécuter les commandes Terraform**

   ```bash
   # Initialiser (télécharge le provider)
   terraform init
   
   # Planifier (voir ce qui va être fait)
   terraform plan
   
   # Appliquer (créer les ressources)
   terraform apply
   # Tapez "yes" pour confirmer
   
   # Vérifier
   cat hello.txt
   
   # Voir l'état
   terraform show
   ```

4. **Modifier et re-appliquer**

   Modifiez la variable :
   ```bash
   terraform apply -var="message=Hello DevOps!"
   cat hello.txt
   ```

5. **Détruire**

   ```bash
   terraform destroy
   # Tapez "yes" pour confirmer
   
   # Vérifier que le fichier est supprimé
   ls hello.txt
   ```

---

## 🧪 Validation

✅ Vous avez réussi si :
- [ ] `terraform init` s'exécute sans erreur
- [ ] `terraform plan` affiche les changements prévus
- [ ] `terraform apply` crée le fichier `hello.txt`
- [ ] `terraform destroy` supprime le fichier

---

## 💡 Indice

**Le workflow Terraform :**
```
terraform init → terraform plan → terraform apply
                      ↓
              (review changes)
                      ↓
              terraform destroy (cleanup)
```

**Toujours** faire un `plan` avant un `apply` pour vérifier !

---

## ✅ Solution

<details>
<summary>Commandes complètes</summary>

```bash
mkdir ~/tf-lab && cd ~/tf-lab

cat > main.tf << 'EOF'
terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}

variable "message" {
  default = "Hello from Terraform!"
}

resource "local_file" "hello" {
  content  = var.message
  filename = "${path.module}/hello.txt"
}

output "file_path" {
  value = local_file.hello.filename
}
EOF

terraform init
terraform plan
terraform apply -auto-approve
cat hello.txt
terraform destroy -auto-approve
```

</details>

---

## 🤖 Test IA

Demandez à une IA :

> *"Écris du code Terraform pour créer une VM Ubuntu sur Azure"*

**Analysez :**
- Le provider est-il correctement configuré ?
- Les credentials sont-ils en dur (mauvaise pratique) ?
- Le code gère-t-il le réseau et les security groups ?

**Leçon** : L'IA génère du code Terraform fonctionnel mais souvent incomplet. Elle oublie souvent les dépendances (réseau, security groups) ou les bonnes pratiques (variables pour les secrets).
