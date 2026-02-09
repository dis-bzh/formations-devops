# 🎯 Exercice 02 : GitHub Actions

> 🟡 Niveau : Intermédiaire | ⏱️ Durée : 60 min

## Objectif

Comprendre le pipeline CI/CD du projet et créer un workflow simple.

## Prérequis

- Compte GitHub
- Fork du repo `denvr` (ou votre propre repo)

## Instructions

### Partie 1 : Analyser les workflows existants (20 min)

1. **Lister les workflows**
   ```bash
   ls -la .github/workflows/
   ```

2. **Analyser `build.yml`**
   Ouvrez le fichier et répondez :

   | Question | Réponse |
   |----------|---------|
   | Quand ce workflow se déclenche-t-il ? | |
   | Quelles permissions sont déclarées ? | |
   | Où l'image est-elle publiée ? | |
   | Quel outil scanne l'image Docker ? | |

3. **Analyser `security.yml`**

   | Question | Réponse |
   |----------|---------|
   | Combien de jobs de sécurité contient-il ? | |
   | Quels types de scan sont effectués ? | |
   | Que fait Gitleaks ? | |

4. **Analyser `deploy.yml`**

   | Question | Réponse |
   |----------|---------|
   | Quel événement le déclenche ? | |
   | Y a-t-il une approbation manuelle ? | |
   | Quels outils sont installés ? | |

### Partie 2 : Créer un workflow simple (30 min)

1. **Créer un nouveau workflow**
   ```bash
   cat > .github/workflows/hello.yml << 'EOF'
   name: Hello World

   on:
     push:
       branches: [main]
     workflow_dispatch:  # Permet de lancer manuellement

   # 🔒 Permissions explicites (bonne pratique DevSecOps)
   permissions:
     contents: read

   jobs:
     greet:
       runs-on: ubuntu-latest
       timeout-minutes: 5  # Évite les jobs qui tournent indéfiniment
       steps:
         - name: Checkout
           uses: actions/checkout@v4

         - name: Say Hello
           run: echo "Hello, ${{ github.actor }}!"

         - name: Show date
           run: date

         - name: List files
           run: ls -la
   EOF
   ```

2. **Comprendre les bonnes pratiques DevSecOps**

   ```yaml
   # ✅ Bonne pratique : permissions explicites
   permissions:
     contents: read  # Seulement ce qui est nécessaire
   
   # ✅ Bonne pratique : timeout
   timeout-minutes: 5
   
   # ✅ Bonne pratique : version pinning
   uses: actions/checkout@v4  # Pas @latest ou @main
   ```

3. **Ajouter une étape de validation**
   
   Modifiez le workflow pour ajouter :
   ```yaml
         - name: Validate Dockerfile exists
           run: |
             if [ -f Dockerfile ]; then
               echo "✅ Dockerfile found"
             else
               echo "❌ Dockerfile missing"
               exit 1
             fi
   ```

### Partie 3 : Comprendre les dépendances (10 min)

Le projet utilise des **dépendances entre workflows** :

```
push tag → build.yml → deploy.yml
              ↓            ↓
         Build image   Terraform + Ansible
         Trivy scan         ↓
              ↓        Deploy to VM
         Push GHCR

Sur chaque push → security.yml
                     ↓
               Snyk + Gitleaks + CodeQL
```

Regardez comment `deploy.yml` attend `build.yml` :
```yaml
on:
  workflow_run:
    workflows: ["Build and Publish Docker image"]
    types: 
      - completed
```

---

## 🔒 Bonnes pratiques DevSecOps dans les pipelines

### Implémentées dans ce projet

| Pratique | Fichier | Description |
|----------|---------|-------------|
| **Permissions explicites** | Tous | `permissions:` avec moindre privilège |
| **Timeouts** | Tous | Évite les jobs infinis |
| **Version pinning** | Tous | `@v4` au lieu de `@latest` |
| **Scan dépendances** | security.yml | Snyk pour Node.js |
| **Scan secrets** | security.yml | Gitleaks |
| **SAST** | security.yml | CodeQL |
| **Scan images** | build.yml | Trivy |
| **Manual approval** | deploy.yml | Avant déploiement |

### À explorer (nice-to-have)

| Pratique | Outil | Description |
|----------|-------|-------------|
| **SBOM** | Syft, Docker SBOM | Inventaire des composants |
| **Image signing** | Cosign | Signature cryptographique |
| **OIDC auth** | GitHub OIDC | Authentification sans secrets |
| **Attestations** | SLSA | Provenance des artefacts |
| **Policy as Code** | OPA, Kyverno | Politiques automatisées |

> 💬 **Discussion** : Quelles pratiques nice-to-have seraient prioritaires dans votre contexte ?

---

## 🧪 Validation

✅ Vous avez réussi si :
- [ ] Vous pouvez expliquer quand chaque workflow se déclenche
- [ ] Votre workflow `hello.yml` s'exécute (si vous avez pushé)
- [ ] Vous comprenez la différence entre `uses:` et `run:`
- [ ] Vous savez pourquoi les `permissions:` sont importantes

---

## 💡 Indice

**Différence `uses` vs `run` :**
- `uses: actions/checkout@v4` → Utilise une **Action** réutilisable (du marketplace GitHub)
- `run: echo "hello"` → Exécute une **commande shell** directe

---

## ✅ Solution

<details>
<summary>Réponses Partie 1</summary>

**build.yml :**
| Question | Réponse |
|----------|---------|
| Déclencheur | Push d'un tag (`tags: '*'`) |
| Permissions | `contents: read`, `packages: write` |
| Registry | `ghcr.io` (GitHub Container Registry) |
| Scan image | Trivy (`aquasecurity/trivy-action`) |

**security.yml :**
| Question | Réponse |
|----------|---------|
| Nombre de jobs | 3 (dependency, secret, sast) |
| Types de scan | Dépendances (Snyk), Secrets (Gitleaks), Code (CodeQL) |
| Gitleaks | Détecte les secrets/clés API dans le code |

**deploy.yml :**
| Question | Réponse |
|----------|---------|
| Déclencheur | `workflow_run` (après build.yml) |
| Approbation manuelle | Oui (`trstringer/manual-approval`) |
| Outils installés | Terraform, Ansible |

</details>

---

## 🤖 Test IA

Demandez à une IA :

> *"Écris un workflow GitHub Actions qui builde une image Docker et la pousse sur Docker Hub"*

**Comparez avec `build.yml` :**
- L'IA déclare-t-elle des `permissions:` explicites ?
- Y a-t-il un scan de sécurité de l'image ?
- Les secrets sont-ils bien référencés ?
- Y a-t-il un `timeout-minutes` ?

**Leçon** : L'IA génère des workflows fonctionnels mais souvent sans les bonnes pratiques de sécurité. Toujours vérifier et compléter !
