# ⚙️ Ansible — Configuration & Hardening

> Support pédagogique pour le **Jour 4** de la formation DevOps/SysOps.

## 📋 Ce que fait ce playbook

Le playbook `playbook.yml` configure et durcit un serveur Ubuntu en 6 étapes :

| # | Étape | Fichier | Type |
|---|-------|---------|------|
| 1 | Installer les paquets (podman, fail2ban) | `tasks/packages.yml` | import_tasks |
| 2 | Créer les utilisateurs + déployer clés SSH | `tasks/users.yml` | import_tasks |
| 3 | Configurer le firewall UFW (règles de ports) | `tasks/ufw.yml` | import_tasks |
| 4 | Configurer Fail2ban (anti brute-force) | `tasks/fail2ban.yml` | import_tasks |
| 5 | Hardening OS (sysctl, filesystem, paquets) | `devsec.hardening.os_hardening` | include_role |
| 6 | Hardening SSH (sshd_config, ciphers) | `devsec.hardening.ssh_hardening` | include_role |

> [!WARNING]
> L'ordre est **crucial** : les tâches de configuration doivent s'exécuter **avant** les rôles
> de hardening. Sinon, le durcissement SSH pourrait verrouiller l'accès (désactivation du
> login par mot de passe avant que les clés SSH soient déployées).

## 🏗️ Structure

```
ansible/
├── ansible.cfg            # Configuration Ansible
├── requirements.yml       # Collections (devsec.hardening, community.general)
├── inventory.example      # Template d'inventaire
├── playbook.yml           # Point d'entrée principal
├── group_vars/
│   └── all.yml            # Variables (users, firewall, hardening)
└── tasks/
    ├── packages.yml       # Installation paquets
    ├── users.yml          # Création users + clés SSH
    ├── ufw.yml            # Règles firewall
    ├── fail2ban.yml       # Anti brute-force
    └── files/
        └── fail2ban/
            └── jail.local # Config fail2ban (sshd)
```

## 🚀 Démarrage rapide

```bash
# 1. Installer les collections requises
ansible-galaxy collection install -r requirements.yml

# 2. Créer l'inventaire à partir du template
cp inventory.example inventory.ini
# Éditer inventory.ini avec l'IP de votre VM (terraform output)

# 3. Éditer les variables (clés SSH, ports, etc.)
nano group_vars/all.yml

# 4. Vérifier sans appliquer (dry-run)
ansible-playbook playbook.yml --check --diff

# 5. Appliquer
ansible-playbook playbook.yml
```

## 📚 Concepts illustrés

| Concept | Où dans ce projet |
|---------|-------------------|
| `import_tasks` | `playbook.yml` → `tasks/*.yml` |
| `include_role` vs `roles:` | Rôles devsec dans `tasks:` pour contrôler l'ordre |
| Variables + boucles | `users.yml` : loop sur la liste `users` |
| Handlers | `fail2ban.yml` → notifie le restart |
| Collections Galaxy | `requirements.yml` → `devsec.hardening` |
| Idempotence | Relancer le playbook = même résultat |

## 🔗 Liens

- [Exercice 11 — Ansible Playbook](../exercises/sysops-j4/11-ansible-playbook.md)
- [Théorie — Ansible & Automatisation](../theory/10-ansible-automation.md)
- [dev-sec/ansible-collection-hardening](https://github.com/dev-sec/ansible-collection-hardening)
