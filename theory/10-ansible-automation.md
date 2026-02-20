# ⚙️ Ansible & Automatisation

> *"Automatiser la configuration, pas l'improvisation."*

## 🎯 Objectifs pédagogiques
- Comprendre l'approche agentless d'Ansible
- Savoir écrire des playbooks, gérer des inventaires
- Connaître les bonnes pratiques : rôles, idempotence, variables

---

## 📖 Pourquoi Ansible ?

### Le problème de la configuration manuelle

```
┌─────────────────────────────────────────────────────┐
│                 SANS AUTOMATISATION                   │
│                                                      │
│  Admin SSH ──► VM1 : apt install, config, restart    │
│  Admin SSH ──► VM2 : apt install, config, restart    │
│  Admin SSH ──► VM3 : oups, j'ai oublié un truc...   │
│                                                      │
│  Problèmes :                                         │
│  - Répétitif et ennuyeux                             │
│  - Erreurs humaines (VM3 ≠ VM1)                      │
│  - Non documenté                                     │
│  - Non reproductible                                 │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│                 AVEC ANSIBLE                         │
│                                                      │
│  Admin ──► playbook.yml ──► VM1, VM2, VM3            │
│                                ssh    ssh    ssh     │
│  Avantages :                                         │
│  - Une seule commande pour tout                      │
│  - Identique sur toutes les machines                 │
│  - Documenté (le code EST la doc)                    │
│  - Reproductible et idempotent                       │
└─────────────────────────────────────────────────────┘
```

---

## 🔧 Qu'est-ce qu'Ansible ?

| Aspect | Détail |
|--------|--------|
| **Créé par** | Michael DeHaan (2012), racheté par Red Hat |
| **Langage** | Playbooks en YAML, modules en Python |
| **Modèle** | Agentless (SSH), déclaratif, idempotent |
| **Licence** | GPL v3 (open source) |

### Agentless : la différence clé

| Aspect | Ansible (agentless) | Chef / Puppet (agent) |
|--------|---------------------|-----------------------|
| **Installation cible** | Rien (SSH suffit) | Agent à installer |
| **Complexité** | Faible | Plus élevée |
| **Sécurité** | SSH standard | Port supplémentaire |
| **Maintenance** | Minimale | Mettre à jour les agents |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                 MACHINE DE CONTRÔLE                  │
│                                                      │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐ │
│  │  Playbook   │  │  Inventory  │  │   ansible    │ │
│  │  (.yml)     │  │  (.ini/.yml)│  │   .cfg       │ │
│  └──────┬──────┘  └──────┬──────┘  └──────────────┘ │
│         │                │                           │
│         └────────┬───────┘                           │
│                  │                                   │
│           ┌──────▼──────┐                            │
│           │   Ansible   │                            │
│           │   Engine    │                            │
│           └──────┬──────┘                            │
└──────────────────┼───────────────────────────────────┘
                   │ SSH
        ┌──────────┼──────────┐
        ▼          ▼          ▼
   ┌─────────┐ ┌─────────┐ ┌─────────┐
   │  VM 1   │ │  VM 2   │ │  VM 3   │
   │ (web)   │ │ (web)   │ │ (db)    │
   └─────────┘ └─────────┘ └─────────┘
```

---

## 📋 Inventaire

L'inventaire liste les machines cibles et les organise en groupes.

### Format INI

```ini
[webservers]
vm-0 ansible_host=192.168.1.10
vm-1 ansible_host=192.168.1.11

[databases]
db-0 ansible_host=192.168.1.20

[all:vars]
ansible_user=deploy
ansible_ssh_private_key_file=~/.ssh/id_ed25519
```

### Inventaire dynamique

En environnement cloud, l'inventaire peut être **généré automatiquement** :
- À partir des **outputs Terraform** (IPs des VMs créées)
- Via des plugins d'inventaire (AWS EC2, Azure, GCP)

> [!TIP]
> Utiliser le **templating Terraform** pour générer l'inventaire Ansible automatiquement.
> C'est le workflow recommandé : Terraform crée → exporte les IPs → Ansible configure.

---

## 📘 Playbooks

Les playbooks décrivent les tâches à exécuter sur les machines cibles.

### Exemple simple

```yaml
---
- name: Configurer les serveurs web
  hosts: webservers
  become: true   # Exécuter en root (sudo)

  tasks:
    - name: Mettre à jour les paquets
      ansible.builtin.package:
        update_cache: true
        upgrade: safe

    - name: Installer Nginx
      ansible.builtin.package:
        name: nginx
        state: present

    - name: Démarrer Nginx
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: true
```

### Exécution

```bash
ansible-playbook -i inventory playbook.yml \
  --private-key ~/.ssh/id_ed25519 \
  -u deploy \
  --ssh-common-args='-o StrictHostKeyChecking=no'
```

---

## 🧩 Modules

Les modules sont les **briques de base** d'Ansible. Préférez toujours un module à une commande shell.

| Module | Usage | Idempotent ? |
|--------|-------|:---:|
| `apt` / `yum` | Installer des paquets | ✅ |
| `service` | Gérer les services (start/stop) | ✅ |
| `copy` | Copier des fichiers statiques | ✅ |
| `template` | Fichiers dynamiques (Jinja2) | ✅ |
| `file` | Créer dossiers, permissions | ✅ |
| `user` | Gérer les utilisateurs | ✅ |
| `command` / `shell` | Exécuter des commandes | ❌ |
| `community.docker.docker_compose` | Gérer Docker Compose | ✅ |

> [!WARNING]
> Les modules `command` et `shell` ne sont **pas idempotents** par défaut.
> Utilisez-les seulement quand aucun module dédié n'existe.
> Privilégiez toujours les modules Ansible et de la communauté pour conserver l'idempotence.

### Templates vs Files

| Besoin | Utiliser | Exemple |
|--------|----------|---------|
| Fichier **statique** (identique partout) | `copy` + `files/` | Certificats, binaires |
| Fichier **dynamique** (variables) | `template` + `templates/` | Configs Nginx, .env |

```yaml
# Template Jinja2 : templates/nginx.conf.j2
server {
    listen {{ nginx_port }};
    server_name {{ server_name }};
}
```

---

## 📂 Rôles

Les rôles structurent les playbooks en composants réutilisables.

```
roles/
└── webserver/
    ├── tasks/
    │   └── main.yml      ← Tâches à exécuter
    ├── templates/
    │   └── nginx.conf.j2 ← Fichiers dynamiques
    ├── files/
    │   └── ssl-cert.pem  ← Fichiers statiques
    ├── vars/
    │   └── main.yml      ← Variables du rôle
    ├── defaults/
    │   └── main.yml      ← Valeurs par défaut
    └── handlers/
        └── main.yml      ← Actions déclenchées (ex: restart)
```

**Utilisation dans un playbook :**

```yaml
---
- hosts: webservers
  become: true
  roles:
    - webserver
    - monitoring
```

> [!TIP]
> **Privilégiez les petits rôles simples** : plus faciles à comprendre, expliquer et maintenir.
> Un rôle = une responsabilité (ex: `docker`, `nginx`, `monitoring`).

---

## 🔐 Ansible Vault

Chiffrer les données sensibles (mots de passe, clés API) :

```bash
# Chiffrer un fichier
ansible-vault encrypt secrets.yml

# Éditer un fichier chiffré
ansible-vault edit secrets.yml

# Exécuter un playbook avec secrets
ansible-playbook playbook.yml --ask-vault-pass
```

---

## ✅ Bonnes pratiques

| Pratique | Pourquoi |
|----------|----------|
| **Variabiliser dès le départ** | Rend les playbooks réutilisables entre projets |
| **Petits rôles spécialisés** | Plus clairs, testables, maintenables |
| **Modules > shell** | Idempotence garantie |
| **Templates pour les configs** | Fichiers dynamiques adaptés à chaque env |
| **`files/` pour le statique** | Fichiers identiques partout |
| **Linting avec `ansible-lint`** | Détecte erreurs et mauvaises pratiques |
| **Tester avec `molecule`** | Tests automatisés des rôles |
| **Valeurs par défaut dans `defaults/`** | Rôles utilisables "out of the box" |

---

## 📊 Terraform + Ansible : le workflow complet

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│ Terraform│     │ Terraform│     │  Ansible  │     │  GitHub  │
│  plan    │────►│  apply   │────►│  playbook │────►│  Actions │
│          │     │          │     │           │     │  (CI/CD) │
│ Vérifier │     │ Créer    │     │ Configurer│     │ Déployer │
│ le plan  │     │ les VMs  │     │ les VMs   │     │ l'app    │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
                       │                │
                       ▼                │
                  outputs.tf ───────────┘
                  (IPs des VMs)
```

---

## ❓ Pourquoi c'est important en 2026 ?

> [!IMPORTANT]
> Ansible reste **incontournable** pour la gestion de configuration :
> - Pas d'agent à maintenir (SSH suffit)
> - Courbe d'apprentissage douce (YAML)
> - Compétence très demandée sur le marché
> - Complémentaire à Terraform (infra + config)

---

## 📚 Sources officielles

| Ressource | Lien |
|-----------|------|
| Ansible Documentation | [docs.ansible.com](https://docs.ansible.com/) |
| Ansible Galaxy (rôles communautaires) | [galaxy.ansible.com](https://galaxy.ansible.com/) |
| Ansible Lint | [ansible.readthedocs.io/projects/lint](https://ansible.readthedocs.io/projects/lint/) |
| Molecule (tests) | [ansible.readthedocs.io/projects/molecule](https://ansible.readthedocs.io/projects/molecule/) |

---

## 🤔 Questions de réflexion

1. Pourquoi l'idempotence est-elle si importante en gestion de configuration ?
2. Quand utiliser Terraform vs Ansible ? Peuvent-ils se remplacer ?
3. Quels sont les avantages d'un système agentless pour la sécurité ?
