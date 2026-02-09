# ☸️ Introduction à Kubernetes

> *"Kubernetes : le système d'exploitation du cloud."*

## 🎯 Objectifs pédagogiques
- Comprendre pourquoi Kubernetes existe
- Connaître l'architecture d'un cluster
- Identifier les objets de base : Pods, Services, Deployments

---

## 📖 Pourquoi Kubernetes ?

### Le problème de l'échelle

```
┌─────────────────────────────────────────────────────┐
│  1 conteneur = facile                               │
│  ┌─────────┐                                        │
│  │  App    │                                        │
│  └─────────┘                                        │
│                                                     │
│  100 conteneurs = difficile                         │
│  ┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐     │
│  │ A ││ A ││ A ││ B ││ B ││ C ││ C ││ C ││ C │...  │
│  └───┘└───┘└───┘└───┘└───┘└───┘└───┘└───┘└───┘     │
│                                                     │
│  Questions :                                        │
│  - Sur quel serveur déployer ?                      │
│  - Que faire si un conteneur crash ?                │
│  - Comment les faire communiquer ?                  │
│  - Comment scaler automatiquement ?                 │
└─────────────────────────────────────────────────────┘
```

### Solution : Orchestration

**Kubernetes** (K8s) est un orchestrateur de conteneurs créé par Google en 2014.

| Fonctionnalité | Description |
|----------------|-------------|
| **Scheduling** | Décide où placer les conteneurs |
| **Self-healing** | Redémarre les conteneurs qui crashent |
| **Service discovery** | Les conteneurs se trouvent automatiquement |
| **Scaling** | Augmente/diminue le nombre de réplicas |
| **Rolling updates** | Déploie sans interruption |

---

## 🏗️ Architecture d'un cluster

```
┌─────────────────────────────────────────────────────────────────┐
│                        CONTROL PLANE                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │ API Server  │  │  Scheduler  │  │ Controller  │              │
│  │             │  │             │  │  Manager    │              │
│  └──────┬──────┘  └─────────────┘  └─────────────┘              │
│         │                                                        │
│  ┌──────▼──────┐                                                │
│  │    etcd     │  ← Base de données du cluster                  │
│  └─────────────┘                                                │
└─────────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│     NODE 1      │ │     NODE 2      │ │     NODE 3      │
│  ┌───────────┐  │ │  ┌───────────┐  │ │  ┌───────────┐  │
│  │  kubelet  │  │ │  │  kubelet  │  │ │  │  kubelet  │  │
│  └───────────┘  │ │  └───────────┘  │ │  └───────────┘  │
│  ┌───────────┐  │ │  ┌───────────┐  │ │  ┌───────────┐  │
│  │ kube-proxy│  │ │  │ kube-proxy│  │ │  │ kube-proxy│  │
│  └───────────┘  │ │  └───────────┘  │ │  └───────────┘  │
│  ┌───┐ ┌───┐   │ │  ┌───┐ ┌───┐   │ │  ┌───┐ ┌───┐   │
│  │Pod│ │Pod│   │ │  │Pod│ │Pod│   │ │  │Pod│ │Pod│   │
│  └───┘ └───┘   │ │  └───┘ └───┘   │ │  └───┘ └───┘   │
└─────────────────┘ └─────────────────┘ └─────────────────┘
```

### Composants

| Composant | Rôle |
|-----------|------|
| **API Server** | Point d'entrée (REST API) |
| **Scheduler** | Assigne les Pods aux Nodes |
| **Controller Manager** | Maintient l'état désiré |
| **etcd** | Base de données clé-valeur |
| **kubelet** | Agent sur chaque node |
| **kube-proxy** | Gestion réseau |

---

## 📦 Objets Kubernetes

### Pod

L'unité de base : un ou plusieurs conteneurs qui partagent réseau et stockage.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-app
spec:
  containers:
  - name: app
    image: python:3.11
    ports:
    - containerPort: 5000
```

### Deployment

Gère les réplicas et les mises à jour de Pods.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app
        image: my-app:v1
```

### Service

Expose les Pods sur le réseau.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 5000
  type: ClusterIP
```

---

## 🛠️ Outils pour apprendre

| Outil | Description |
|-------|-------------|
| **kind** | Kubernetes in Docker (local) |
| **minikube** | Cluster local simple |
| **k3s** | Version légère de K8s |
| **Docker Desktop** | Inclut K8s (Windows/Mac) |

### Démo locale avec kind

```bash
# Installer kind
curl -Lo ./kind https://kind.sigs.k8s.io/dl/latest/kind-linux-amd64
chmod +x ./kind && mv ./kind /usr/local/bin/

# Créer un cluster
kind create cluster --name demo

# Vérifier
kubectl get nodes

# Supprimer
kind delete cluster --name demo
```

---

## ⚠️ Kubernetes dans cette formation

> [!WARNING]
> Kubernetes est **complexe** et nécessite du temps pour être maîtrisé.
> 
> Dans cette formation (2 jours SysOps) :
> - **Théorie** : Comprendre l'architecture et les concepts
> - **Démo** : Voir K8s en action (kind local)
> - **Pas de hands-on** : Le focus reste sur Docker et CI/CD

---

## 📚 Sources officielles

| Ressource | Lien |
|-----------|------|
| Kubernetes Documentation | [kubernetes.io/docs](https://kubernetes.io/docs/) |
| Kubernetes The Hard Way | [github.com/kelseyhightower](https://github.com/kelseyhightower/kubernetes-the-hard-way) |
| kind | [kind.sigs.k8s.io](https://kind.sigs.k8s.io/) |
| CNCF | [cncf.io](https://www.cncf.io/) |

---

## 🤔 Questions de réflexion

1. Pourquoi ne pas utiliser Docker Compose pour la production ?
2. Qu'est-ce qui rend Kubernetes complexe à apprendre ?
3. Kubernetes est-il toujours la bonne solution ?
