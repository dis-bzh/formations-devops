# 🎯 Exercice 10 - Démo Kubernetes

> **Objectif** : Observer Kubernetes en action avec un cluster local

## 📋 Contexte

Kubernetes est complexe, mais comprendre ses concepts de base est essentiel. Cette démo utilise **kind** (Kubernetes in Docker) pour créer un cluster local.

> [!NOTE]
> Ceci est une **démo guidée par le formateur**. Suivez les commandes ensemble.

---

## 🎯 Mission

1. Observer la création d'un cluster
2. Déployer une application simple
3. Comprendre les objets de base (Pod, Deployment, Service)

---

## 📝 Démo

### Partie 1 : Créer un cluster

```bash
# Vérifier que kind est installé
kind --version

# Créer un cluster
kind create cluster --name demo

# Vérifier la connexion
kubectl cluster-info

# Voir les nodes
kubectl get nodes
```

### Partie 2 : Explorer le cluster

```bash
# Voir tous les namespaces
kubectl get namespaces

# Voir les pods système
kubectl get pods -n kube-system

# Voir les composants
kubectl get componentstatuses  # (déprécié mais instructif)
```

### Partie 3 : Déployer une application

```bash
# Créer un déploiement nginx
kubectl create deployment web --image=nginx

# Voir le déploiement
kubectl get deployments

# Voir le pod créé
kubectl get pods

# Voir les détails du pod
kubectl describe pod <nom-du-pod>
```

### Partie 4 : Scaler l'application

```bash
# Passer à 3 réplicas
kubectl scale deployment web --replicas=3

# Observer les nouveaux pods
kubectl get pods

# Observer la distribution
kubectl get pods -o wide
```

### Partie 5 : Exposer l'application

```bash
# Créer un service
kubectl expose deployment web --port=80 --type=NodePort

# Voir le service
kubectl get services

# Accéder via port forward (plus simple avec kind)
kubectl port-forward service/web 8888:80 &

# Tester
curl http://localhost:8888
```

### Partie 6 : Observer le self-healing

```bash
# Supprimer un pod
kubectl delete pod <nom-d-un-pod>

# Observer immédiatement
kubectl get pods

# Kubernetes recrée automatiquement le pod !
```

### Partie 7 : YAML déclaratif

Créer un fichier `deployment.yaml` :

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello
spec:
  replicas: 2
  selector:
    matchLabels:
      app: hello
  template:
    metadata:
      labels:
        app: hello
    spec:
      containers:
      - name: hello
        image: gcr.io/google-samples/hello-app:1.0
        ports:
        - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: hello
spec:
  selector:
    app: hello
  ports:
  - port: 80
    targetPort: 8080
  type: ClusterIP
```

```bash
# Appliquer la configuration
kubectl apply -f deployment.yaml

# Voir les ressources créées
kubectl get all -l app=hello
```

---

## 🔑 Concepts clés observés

| Concept | Ce que vous avez vu |
|---------|---------------------|
| **Pod** | Unité de base, contient le conteneur |
| **Deployment** | Gère les réplicas et mises à jour |
| **Service** | Expose les pods sur le réseau |
| **Self-healing** | Kubernetes recrée les pods supprimés |
| **Scaling** | Augmente/diminue facilement les réplicas |
| **Déclaratif** | On décrit l'état désiré, K8s s'en occupe |

---

## ❓ Questions de discussion

1. Quelle différence avez-vous observée entre `kubectl create` et `kubectl apply` ?
2. Comment Kubernetes sait-il quel pod appartient à quel service ?
3. Pourquoi utiliser Kubernetes plutôt que juste Docker Compose ?

---

## 🧹 Nettoyage

```bash
# Supprimer les ressources
kubectl delete -f deployment.yaml
kubectl delete deployment web
kubectl delete service web

# Supprimer le cluster
kind delete cluster --name demo
```

---

## 📚 Ressources

- [Théorie : Introduction à Kubernetes](../../theory/08-kubernetes-intro.md)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [kind Quick Start](https://kind.sigs.k8s.io/docs/user/quick-start/)
