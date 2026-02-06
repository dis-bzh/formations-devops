# 🎯 Exercice 04 : GitHub Actions

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
   | Combien de jobs contient-il ? | |
   | Où l'image est-elle publiée ? | |
   | Quel secret est utilisé pour l'authentification ? | |

3. **Analyser `deploy.yml`**

   | Question | Réponse |
   |----------|---------|
   | Quel événement le déclenche ? | |
   | Y a-t-il une approbation manuelle ? | |
   | Quels outils sont installés ? | |

4. **Analyser `snyk.yml`**

   | Question | Réponse |
   |----------|---------|
   | Quand s'exécute-t-il ? | |
   | Que scanne-t-il ? | |
   | Le build échoue-t-il si des vulnérabilités sont trouvées ? | |

### Partie 2 : Créer un workflow simple (30 min)

1. **Créer un nouveau workflow**
   ```bash
   cat > .github/workflows/hello.yml << 'EOF'
   name: Hello World

   on:
     push:
       branches: [main]
     workflow_dispatch:  # Permet de lancer manuellement

   jobs:
     greet:
       runs-on: ubuntu-latest
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

2. **Comprendre la syntaxe**

   ```yaml
   name: Hello World          # Nom du workflow
   
   on:                        # Déclencheurs
     push:
       branches: [main]       # Sur push vers main
     workflow_dispatch:       # + bouton manuel
   
   jobs:                      # Liste des jobs
     greet:                   # Nom du job
       runs-on: ubuntu-latest # Runner
       steps:                 # Étapes du job
         - name: Checkout     # Nom de l'étape
           uses: actions/checkout@v4  # Action réutilisable
         
         - name: Say Hello
           run: echo "..."    # Commande shell
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
              ↓            ↓
         Push GHCR    Deploy to VM
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

## 🧪 Validation

✅ Vous avez réussi si :
- [ ] Vous pouvez expliquer quand chaque workflow se déclenche
- [ ] Votre workflow `hello.yml` s'exécute (si vous avez pushé)
- [ ] Vous comprenez la différence entre `uses:` et `run:`

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
| Nombre de jobs | 2 (version + docker) |
| Registry | `ghcr.io` (GitHub Container Registry) |
| Secret auth | `GITHUB_TOKEN` (automatique) |

**deploy.yml :**
| Question | Réponse |
|----------|---------|
| Déclencheur | `workflow_run` (après build.yml) |
| Approbation manuelle | Oui (`trstringer/manual-approval`) |
| Outils installés | Terraform, Ansible |

**snyk.yml :**
| Question | Réponse |
|----------|---------|
| Déclencheur | Tout push (`on: push`) |
| Cible scan | Application Node.js (`my-app`) |
| Bloquant | Non (`continue-on-error: true`) ⚠️ |

</details>

---

## 🤖 Test IA

Demandez à une IA :

> *"Écris un workflow GitHub Actions qui builde une image Docker et la pousse sur Docker Hub"*

**Comparez avec `build.yml` :**
- L'IA utilise-t-elle le cache (`cache-from: type=gha`) ?
- Le tagging utilise-t-il la version sémantique ?
- Les secrets sont-ils bien référencés ?

**Leçon** : L'IA génère des workflows fonctionnels mais basiques. Les optimisations (cache, versioning, multi-plateforme) nécessitent une connaissance des bonnes pratiques.
