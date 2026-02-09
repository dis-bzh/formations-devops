# 📊 Monitoring et SRE

> *"You can't improve what you don't measure."*

## 🎯 Objectifs pédagogiques
- Comprendre les concepts de monitoring et observabilité
- Découvrir le rôle du Site Reliability Engineering (SRE)
- Connaître les métriques clés : SLI, SLO, SLA

---

## 📖 Définitions

### Monitoring vs Observabilité

| Concept | Description | Question |
|---------|-------------|----------|
| **Monitoring** | Surveiller des métriques connues | "Est-ce que ça marche ?" |
| **Observabilité** | Comprendre l'état interne via outputs | "Pourquoi ça ne marche pas ?" |

### Les 3 piliers de l'observabilité

```
┌─────────────────────────────────────────────────────┐
│                  OBSERVABILITÉ                       │
├─────────────────┬─────────────────┬─────────────────┤
│     METRICS     │      LOGS       │     TRACES      │
│                 │                 │                 │
│  CPU: 85%       │  [ERROR] DB     │  Request A      │
│  Memory: 2GB    │  connection     │    → Service B  │
│  Requests: 100/s│  timeout at...  │    → Database   │
│                 │                 │    → Response   │
└─────────────────┴─────────────────┴─────────────────┘
```

| Pilier | Ce que c'est | Exemple |
|--------|--------------|---------|
| **Metrics** | Valeurs numériques dans le temps | CPU, RAM, latence, erreurs |
| **Logs** | Événements textuels horodatés | Erreurs, warnings, infos |
| **Traces** | Parcours d'une requête | Request → Services → Response |

---

## 🏗️ Site Reliability Engineering (SRE)

### Origine

- Créé par **Google** en 2003
- Ben Treynor Sloss : *"SRE is what happens when you ask a software engineer to design an operations team."*

### Principes clés

| Principe | Description |
|----------|-------------|
| **Error budgets** | Quantité d'erreurs "acceptables" |
| **Éliminer le toil** | Automatiser les tâches répétitives |
| **Blameless post-mortems** | Apprendre sans accuser |
| **Gradual rollouts** | Déployer progressivement |

---

## 📏 SLI, SLO, SLA

### Définitions

| Terme | Signification | Exemple |
|-------|---------------|---------|
| **SLI** | Service Level Indicator | Latence p99, taux d'erreur |
| **SLO** | Service Level Objective | "99.9% des requêtes < 200ms" |
| **SLA** | Service Level Agreement | Contrat avec pénalités |

### Exemple concret

```
┌─────────────────────────────────────────────────────┐
│  Service: API de paiement                           │
├─────────────────────────────────────────────────────┤
│  SLI: % requêtes réussies (HTTP 2xx)                │
│  SLO: 99.95% de succès sur 30 jours                 │
│  SLA: Si < 99.9%, crédit client 10%                 │
├─────────────────────────────────────────────────────┤
│  Error Budget: 0.05% = ~22 minutes de downtime/mois │
└─────────────────────────────────────────────────────┘
```

---

## 🛠️ Outils de monitoring

| Catégorie | Outils | Description |
|-----------|--------|-------------|
| **Metrics** | Prometheus, Datadog, CloudWatch | Collecter et visualiser métriques |
| **Logs** | ELK Stack, Loki, Splunk | Centraliser et rechercher logs |
| **Traces** | Jaeger, Zipkin, Datadog APM | Tracer les requêtes distribuées |
| **Alerting** | PagerDuty, Opsgenie, Alertmanager | Notifier en cas de problème |
| **Dashboards** | Grafana, Kibana | Visualiser les données |

### Stack simple recommandée

```
Application ──► Prometheus (metrics) ──► Grafana (dashboards)
     │
     └────────► Loki (logs) ─────────────┘
```

---

## 📊 Métriques essentielles

### Les 4 Golden Signals (Google SRE)

| Signal | Description | Exemple |
|--------|-------------|---------|
| **Latency** | Temps de réponse | p50, p95, p99 |
| **Traffic** | Volume de requêtes | req/sec |
| **Errors** | Taux d'erreurs | % 5xx |
| **Saturation** | Utilisation ressources | CPU, RAM, disque |

### RED Method (pour microservices)

| Métrique | Description |
|----------|-------------|
| **Rate** | Requêtes par seconde |
| **Errors** | Erreurs par seconde |
| **Duration** | Durée des requêtes |

---

## ❓ Pourquoi c'est important en 2026 ?

> [!IMPORTANT]
> Le monitoring est **critique** car :
> - Les systèmes distribués sont complexes
> - Les utilisateurs attendent 99.99% de disponibilité
> - Le debugging sans observabilité est impossible

---

## 📚 Sources officielles

| Ressource | Lien |
|-----------|------|
| Google SRE Book | [sre.google/books](https://sre.google/books/) |
| Prometheus Docs | [prometheus.io/docs](https://prometheus.io/docs/) |
| Grafana Docs | [grafana.com/docs](https://grafana.com/docs/) |
| OpenTelemetry | [opentelemetry.io](https://opentelemetry.io/) |

---

## 🤔 Questions de réflexion

1. Quelle est la différence entre monitoring et observabilité ?
2. Pourquoi les "error budgets" sont-ils utiles ?
3. Comment choisir les bons SLI pour votre application ?
