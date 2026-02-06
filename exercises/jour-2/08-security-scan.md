# 🎯 Exercice 08 : Security Scan

> 🟡 Niveau : Intermédiaire | ⏱️ Durée : 30 min

## Objectif

Comprendre l'importance du DevSecOps et scanner les vulnérabilités.

## Prérequis

- Node.js installé (pour Snyk)
- Compte Snyk gratuit (optionnel)

## Instructions

### Partie 1 : Comprendre DevSecOps (10 min)

**DevSecOps = Dev + Sec + Ops**

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│   Dev   │────►│   Sec   │────►│   Ops   │
│  Code   │     │  Scan   │     │ Deploy  │
└─────────┘     └─────────┘     └─────────┘
     │               │               │
     └───────────────┴───────────────┘
         Intégré, pas en silo !
```

**Types de scans :**

| Type | Cible | Outils |
|------|-------|--------|
| **SAST** | Code source | SonarQube, Snyk Code |
| **SCA** | Dépendances | Snyk, Dependabot, Trivy |
| **DAST** | App en cours d'exécution | OWASP ZAP |
| **Container** | Images Docker | Trivy, Grype |
| **IaC** | Terraform, Ansible | Checkov, tfsec |

### Partie 2 : Analyser le workflow Snyk (10 min)

1. **Ouvrir le fichier**
   ```bash
   cat .github/workflows/snyk.yml
   ```

2. **Identifier le problème**

   ```yaml
   - name: Run Snyk to check for vulnerabilities
     uses: snyk/actions/node@master
     continue-on-error: true  # ⚠️ PROBLÈME !
   ```

   > `continue-on-error: true` signifie que le build **continue même si des vulnérabilités sont trouvées** !

3. **Réflexion**

   | Question | Réponse |
   |----------|---------|
   | Le scan est-il bloquant actuellement ? | Non |
   | Devrait-il l'être en production ? | Oui |
   | Pourquoi quelqu'un mettrait-il `continue-on-error` ? | Tests, early stage |

### Partie 3 : Scanner localement (10 min)

**Option A : Avec npm audit (intégré)**

```bash
cd my-app
npm audit

# Voir le détail
npm audit --audit-level=high
```

**Option B : Avec Snyk CLI**

```bash
# Installer Snyk
npm install -g snyk

# Authentification (optionnel, limite sinon)
snyk auth

# Scanner
cd my-app
snyk test
```

**Option C : Avec Trivy (images Docker)**

```bash
# Installer Trivy
sudo apt install trivy

# Scanner l'image du projet
docker build -t denvr-app:test .
trivy image denvr-app:test
```

### Partie 4 : Corriger le workflow (bonus)

Modifiez `.github/workflows/snyk.yml` pour rendre le scan bloquant :

```yaml
name: Security scan with Snyk

on: push

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Snyk to check for vulnerabilities
        uses: snyk/actions/node@master
        # Retirer continue-on-error pour bloquer
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          args: --severity-threshold=high --workdir=/github/workspace/my-app

      - name: Upload Snyk report
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: snyk-report
          path: snyk-report.json
```

---

## 🧪 Validation

✅ Vous avez réussi si :
- [ ] Vous avez exécuté un scan de vulnérabilités
- [ ] Vous comprenez la différence entre un scan bloquant et non-bloquant
- [ ] Vous pouvez expliquer pourquoi `continue-on-error: true` est dangereux

---

## 💡 Indice

**Niveaux de sévérité :**
- `low` : Risque minimal
- `medium` : À corriger quand possible
- `high` : À corriger rapidement
- `critical` : À corriger immédiatement

En production, bloquezau moins les `high` et `critical`.

---

## ✅ Solution

<details>
<summary>Résultats attendus npm audit</summary>

```bash
$ npm audit

# Severity: critical, high, moderate, low
┌───────────────┬──────────────────────────────────────────────────────────────┐
│ high          │ Prototype Pollution in xyz-package                           │
├───────────────┼──────────────────────────────────────────────────────────────┤
│ Package       │ xyz-package                                                  │
├───────────────┼──────────────────────────────────────────────────────────────┤
│ Dependency of │ some-framework                                               │
├───────────────┼──────────────────────────────────────────────────────────────┤
│ Path          │ some-framework > xyz-package                                 │
├───────────────┼──────────────────────────────────────────────────────────────┤
│ More info     │ https://github.com/advisories/GHSA-xxxx-xxxx-xxxx            │
└───────────────┴──────────────────────────────────────────────────────────────┘

found X vulnerabilities (Y critical, Z high, ...)
```

</details>

---

## 🤖 Test IA

Demandez à une IA :

> *"J'ai une vulnérabilité high dans lodash, comment la corriger ?"*

**Analysez :**
- L'IA donne-t-elle la version spécifique à utiliser ?
- Mentionne-t-elle que ça peut être une dépendance transitive ?
- Propose-t-elle `npm audit fix` ou une autre méthode ?

**Leçon** : L'IA donne des conseils génériques. Pour les vulnérabilités spécifiques, consultez toujours l'advisory officiel (lien dans le rapport).
