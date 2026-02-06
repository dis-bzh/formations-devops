# ☁️ Cloud Computing - Fondamentaux

> *"Le cloud, c'est juste l'ordinateur de quelqu'un d'autre."* — Mais en beaucoup plus complexe !

## 🎯 Objectifs pédagogiques
- Comprendre l'origine et l'évolution du cloud
- Maîtriser la définition officielle NIST
- Distinguer IaaS, PaaS, SaaS

---

## 📅 Chronologie

### Avant le Cloud : L'ère des datacenters (< 2006)

```
┌─────────────────────────────────────────────────────┐
│                   DATACENTER                        │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐   │
│  │ SRV │ │ SRV │ │ SRV │ │ SRV │ │ SRV │ │ SRV │   │
│  └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘   │
│    │       │       │       │       │       │       │
│    └───────┴───────┴───────┴───────┴───────┘       │
│                        │                           │
│              Coût: $$$$ + 6 mois de délai          │
└─────────────────────────────────────────────────────┘
```

**Problèmes :**
- **Coûts initiaux énormes** (CAPEX)
- **Délais** : Commander un serveur = semaines/mois
- **Sous-utilisation** : Serveurs dimensionnés pour les pics
- **Gestion manuelle** de tout

### 2006 : Amazon lance AWS

| Date | Service | Description |
|------|---------|-------------|
| Mars 2006 | **S3** | Simple Storage Service |
| Juillet 2006 | **SQS** | Simple Queue Service |
| Août 2006 | **EC2** | Elastic Compute Cloud |

> [!NOTE]
> Amazon a créé AWS pour rentabiliser sa propre infrastructure e-commerce sous-utilisée hors pics (Black Friday).

### 2008-2010 : Les concurrents arrivent

- **2008** : Google App Engine (PaaS)
- **2010** : Microsoft Azure
- **2011** : Google Compute Engine

### 2011 : Définition officielle NIST

Le **NIST** (National Institute of Standards and Technology) publie la **SP 800-145** : définition officielle du cloud computing.

---

## 📖 Définition NIST (SP 800-145)

> *"Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction."*

### Les 5 caractéristiques essentielles

| # | Caractéristique | Explication |
|---|-----------------|-------------|
| 1 | **On-demand self-service** | Je peux provisionner sans intervention humaine |
| 2 | **Broad network access** | Accessible via le réseau (API, web) |
| 3 | **Resource pooling** | Ressources mutualisées entre clients |
| 4 | **Rapid elasticity** | Scale up/down automatique |
| 5 | **Measured service** | Facturation à l'usage |

### Les 3 modèles de service

```
┌─────────────────────────────────────────────────────────────────┐
│                           SaaS                                  │
│     (Gmail, Office 365, Salesforce)                             │
│     Tu utilises l'application                                   │
├─────────────────────────────────────────────────────────────────┤
│                           PaaS                                  │
│     (Heroku, Google App Engine, Azure App Service)              │
│     Tu gères le code, le cloud gère le reste                    │
├─────────────────────────────────────────────────────────────────┤
│                           IaaS                                  │
│     (EC2, Azure VMs, GCE, Denv-r)                               │
│     Tu gères tout sauf le hardware                              │
├─────────────────────────────────────────────────────────────────┤
│                      Infrastructure                             │
│     (Hardware, Datacenter, Réseau)                              │
│     Le cloud provider gère                                      │
└─────────────────────────────────────────────────────────────────┘

    Plus on monte ──────────────────────► Moins de contrôle
                                          Plus de simplicité
```

### Les 4 modèles de déploiement

| Modèle | Description | Exemple |
|--------|-------------|---------|
| **Public** | Ressources partagées, multi-tenant | AWS, Azure, GCP |
| **Private** | Dédié à une organisation | VMware, OpenStack on-premise |
| **Hybrid** | Mix public + private | Azure Stack, AWS Outposts |
| **Community** | Partagé entre organisations similaires | Cloud gouvernemental |

---

## 💰 Modèle économique : CAPEX vs OPEX

| Aspect | Avant (CAPEX) | Après (OPEX) |
|--------|---------------|--------------|
| **Investissement** | Achat serveurs upfront | Paiement à l'usage |
| **Risque** | Risque de sur/sous-dimension | Élasticité |
| **Comptabilité** | Immobilisation | Charge d'exploitation |
| **Délai** | Semaines/mois | Minutes |

---

## ❓ Pourquoi c'est important en 2026 ?

> [!IMPORTANT]
> Comprendre le cloud est **essentiel** car :
> - 94% des entreprises utilisent du cloud (2025)
> - Les compétences cloud sont les plus demandées
> - L'IA s'appuie massivement sur l'infrastructure cloud

---

## 📚 Sources officielles

| Ressource | Lien |
|-----------|------|
| NIST SP 800-145 | [csrc.nist.gov](https://csrc.nist.gov/publications/detail/sp/800-145/final) |
| AWS History | [aws.amazon.com/about-aws](https://aws.amazon.com/about-aws/) |
| Cloud Native Computing Foundation | [cncf.io](https://www.cncf.io/) |

---

## 🤔 Questions de réflexion

1. Pourquoi Amazon (un site e-commerce) est-il devenu leader du cloud ?
2. Quelle est la différence entre héberger sur un VPS et utiliser du "vrai" cloud ?
3. Quels sont les risques de dépendre d'un seul cloud provider (vendor lock-in) ?
