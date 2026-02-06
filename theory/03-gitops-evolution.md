# 🔄 De DevOps à GitOps

> *"Git est la source de vérité pour tout."*

## 🎯 Objectifs pédagogiques
- Comprendre l'évolution DevOps → GitOps
- Maîtriser les principes du GitOps
- Connaître les outils : Flux CD, Argo CD

---

## 📅 Évolution

### DevOps classique : Push-based

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    Dev      │────►│    CI/CD    │────►│   Cluster   │
│  git push   │     │   Jenkins   │     │   K8s/VMs   │
└─────────────┘     └─────────────┘     └─────────────┘
                           │
                           ▼
                    "Je pousse vers
                     la production"
```

**Problèmes du modèle push :**
- CI/CD a des credentials pour accéder à la prod
- Difficile de savoir l'état réel vs désiré
- Pas d'auto-healing si quelqu'un modifie manuellement

### 2017 : Weaveworks invente GitOps

**Alexis Richardson** (CEO Weaveworks) crée le terme **GitOps** pour décrire comment ils gèrent Kubernetes.

> *"GitOps is an operating model for cloud native applications, using Git as the source of truth."*

### GitOps : Pull-based

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    Dev      │────►│    Git      │◄────│  GitOps     │
│  git push   │     │   Repo      │     │  Operator   │
└─────────────┘     └─────────────┘     └─────────────┘
                                               │
                                               ▼
                                        ┌─────────────┐
                                        │   Cluster   │
                                        │   K8s/VMs   │
                                        └─────────────┘
                                               │
                                               ▼
                                    "Je me réconcilie
                                     avec ce que dit Git"
```

---

## 🔑 Les 4 principes GitOps

| # | Principe | Description |
|---|----------|-------------|
| 1 | **Déclaratif** | Tout est décrit de manière déclarative (YAML, HCL...) |
| 2 | **Versionné dans Git** | Git = source of truth unique |
| 3 | **Appliqué automatiquement** | L'agent GitOps réconcilie automatiquement |
| 4 | **Réconciliation continue** | L'état réel converge vers l'état désiré |

### Avantages

| Avantage | Explication |
|----------|-------------|
| **Auditabilité** | Tout changement = commit Git avec auteur, date, message |
| **Rollback facile** | `git revert` pour annuler un changement |
| **Sécurité** | L'agent pull depuis Git, pas de credentials CI vers prod |
| **Auto-healing** | Si quelqu'un modifie manuellement, l'agent corrige |

---

## 🛠️ Outils GitOps

### Flux CD

| Aspect | Détail |
|--------|--------|
| **Créé par** | Weaveworks (2016) |
| **Status** | CNCF Graduated Project |
| **Spécialité** | Kubernetes-native, modulaire |
| **Site** | [fluxcd.io](https://fluxcd.io) |

```yaml
# Exemple Flux: GitRepository
apiVersion: source.toolkit.fluxcd.io/v1
kind: GitRepository
metadata:
  name: my-app
spec:
  interval: 1m
  url: https://github.com/org/my-app
  ref:
    branch: main
```

### Argo CD

| Aspect | Détail |
|--------|--------|
| **Créé par** | Intuit (2018) |
| **Status** | CNCF Graduated Project |
| **Spécialité** | UI riche, multi-cluster |
| **Site** | [argo-cd.readthedocs.io](https://argo-cd.readthedocs.io) |

```yaml
# Exemple Argo CD: Application
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
spec:
  project: default
  source:
    repoURL: https://github.com/org/my-app
    targetRevision: HEAD
    path: k8s
  destination:
    server: https://kubernetes.default.svc
    namespace: production
```

### Comparaison

| Critère | Flux CD | Argo CD |
|---------|---------|---------|
| **UI** | Minimale (extensions) | Riche, native |
| **Architecture** | Modulaire (toolkit) | Monolithique |
| **Multi-tenant** | Via namespaces | Application Projects |
| **Courbe apprentissage** | Modérée | Facile |

---

## 🔗 GitOps dans ce repo

Ce repository utilise des concepts GitOps :

```
git push tag ──► GitHub Actions ──► Build image ──► Push registry
                                                         │
                                                         ▼
                             Ansible déploie depuis le registry
```

> [!NOTE]
> C'est du **GitOps simplifié** : le déclencheur est Git, mais le déploiement reste push-based via Ansible.
> Un "vrai" GitOps utiliserait Flux ou Argo qui **tire** (pull) les changements.

---

## ❓ Pourquoi c'est important en 2026 ?

> [!IMPORTANT]
> GitOps est devenu le **standard de facto** pour Kubernetes :
> - Adopté par les grandes entreprises
> - Requis pour les certifications (CKA, CKAD avancé)
> - Base de la plupart des plateformes DevOps modernes

---

## 📚 Sources officielles

| Ressource | Lien |
|-----------|------|
| GitOps.tech (principes) | [gitops.tech](https://www.gitops.tech) |
| Flux CD Documentation | [fluxcd.io/docs](https://fluxcd.io/docs/) |
| Argo CD Documentation | [argo-cd.readthedocs.io](https://argo-cd.readthedocs.io) |
| OpenGitOps (CNCF) | [opengitops.dev](https://opengitops.dev) |
| Weaveworks Blog (origine) | [weave.works/blog](https://www.weave.works/technologies/gitops/) |

---

## 🤔 Questions de réflexion

1. Quelle est la différence entre CI/CD "classique" et GitOps ?
2. Pourquoi le modèle "pull" est-il plus sécurisé que le modèle "push" ?
3. GitOps est-il applicable sans Kubernetes ?
