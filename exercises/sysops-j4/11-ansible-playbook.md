# 🎯 Exercice 11 : Ansible Playbook

> 🟡 Niveau : Intermédiaire | ⏱️ Durée : 45 min

## Objectif

Configurer des serveurs avec Ansible de manière reproducible.

## Prérequis

- Ansible installé (`ansible --version`)
- Une VM accessible en SSH (exercice 05) OU Docker pour tester localement

## Instructions

### Partie 1 : Comprendre Ansible (10 min)

**Qu'est-ce qu'Ansible ?**

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Playbook      │────►│    Ansible      │────►│    Serveur(s)   │
│   (YAML)        │     │    (SSH)        │     │    Remote       │
└─────────────────┘     └─────────────────┘     └─────────────────┘

    Déclaratif           Idempotent            Configuration
```

**Concepts clés :**

| Concept | Description | Exemple |
|---------|-------------|---------|
| **Inventory** | Liste des serveurs | `hosts`, fichiers INI/YAML |
| **Playbook** | Liste de tâches | `playbook.yml` |
| **Task** | Action unitaire | Installer un paquet |
| **Module** | Type d'action | `apt`, `copy`, `service` |
| **Handler** | Réaction à un changement | Restart nginx |

### Partie 2 : Analyser les playbooks existants (15 min)

1. **Explorer le dossier Ansible**
   ```bash
   cd ansible
   ls -la
   cat playbook.yml
   ```

2. **Comprendre la structure**

   ```yaml
   ---
   - name: denvr              # Nom du play
     hosts: all               # Cibles (depuis l'inventory)
     tasks:                   # Liste des tâches
       - name: Include task list in play
         ansible.builtin.import_tasks:
           file: tasks/packages.yml
         become: true         # = sudo
   ```

3. **Analyser les tâches**

   ```bash
   cat tasks/packages.yml
   cat tasks/ufw.yml
   cat tasks/fail2ban.yml
   ```

   | Fichier | Actions | Module utilisé |
   |---------|---------|----------------|
   | `packages.yml` | Update, Docker, fail2ban | `apt` |
   | `ufw.yml` | Firewall enable, règles | `community.general.ufw` |
   | `fail2ban.yml` | Start, enable, config | `service`, `copy` |

### Partie 3 : Exécuter un playbook local (20 min)

On va tester Ansible en local (sans serveur distant).

1. **Créer un dossier de travail**
   ```bash
   mkdir ~/ansible-lab && cd ~/ansible-lab
   ```

2. **Créer un inventory local**
   ```bash
   cat > inventory << 'EOF'
   [local]
   localhost ansible_connection=local
   EOF
   ```

3. **Créer un playbook simple**
   ```bash
   cat > playbook.yml << 'EOF'
   ---
   - name: Configuration locale
     hosts: local
     tasks:
       - name: Afficher un message
         ansible.builtin.debug:
           msg: "Bonjour depuis Ansible!"

       - name: Créer un fichier
         ansible.builtin.copy:
           content: "Créé par Ansible le {{ ansible_date_time.iso8601 }}"
           dest: /tmp/ansible-test.txt

       - name: Vérifier que le fichier existe
         ansible.builtin.stat:
           path: /tmp/ansible-test.txt
         register: file_stat

       - name: Afficher le résultat
         ansible.builtin.debug:
           msg: "Fichier existe: {{ file_stat.stat.exists }}"
   EOF
   ```

4. **Exécuter**
   ```bash
   ansible-playbook -i inventory playbook.yml
   ```

5. **Vérifier**
   ```bash
   cat /tmp/ansible-test.txt
   ```

6. **Ré-exécuter** (idempotence)
   ```bash
   ansible-playbook -i inventory playbook.yml
   ```
   > Notez le "changed" vs "ok". Ansible ne recrée pas ce qui existe déjà !

### Partie 4 : Playbook avancé (optionnel)

```yaml
---
- name: Installation LAMP basique
  hosts: local
  become: true  # Nécessite sudo
  vars:
    packages:
      - nginx
      - git
      - curl
  tasks:
    - name: Installation des paquets
      ansible.builtin.apt:
        name: "{{ packages }}"
        state: present
        update_cache: true

    - name: Nginx est démarré
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: true
```

---

## 🧪 Validation

✅ Vous avez réussi si :
- [ ] `ansible-playbook` s'exécute sans erreur
- [ ] Le fichier `/tmp/ansible-test.txt` est créé
- [ ] La ré-exécution montre "ok" au lieu de "changed"

---

## 💡 Indice

**L'idempotence** = exécuter plusieurs fois donne le même résultat.

C'est la force d'Ansible : vous déclarez l'état souhaité, Ansible s'assure qu'il est atteint sans tout refaire à chaque fois.

---

## ✅ Solution

<details>
<summary>Commandes complètes</summary>

```bash
mkdir ~/ansible-lab && cd ~/ansible-lab

cat > inventory << 'EOF'
[local]
localhost ansible_connection=local
EOF

cat > playbook.yml << 'EOF'
---
- name: Configuration locale
  hosts: local
  tasks:
    - name: Afficher un message
      ansible.builtin.debug:
        msg: "Bonjour depuis Ansible!"

    - name: Créer un fichier
      ansible.builtin.copy:
        content: "Créé par Ansible le {{ ansible_date_time.iso8601 }}"
        dest: /tmp/ansible-test.txt

    - name: Vérifier que le fichier existe
      ansible.builtin.stat:
        path: /tmp/ansible-test.txt
      register: file_stat

    - name: Afficher le résultat
      ansible.builtin.debug:
        msg: "Fichier existe: {{ file_stat.stat.exists }}"
EOF

ansible-playbook -i inventory playbook.yml
cat /tmp/ansible-test.txt
```

</details>

---

## Partie 5 — Collections Galaxy & Hardening (30 min)

> [!TIP]
> En entreprise, on ne réinvente pas la roue. On utilise des rôles et collections
> communautaires maintenus par la communauté. Ansible Galaxy est le "npm/pip" d'Ansible.

### 5.1 Installer une collection externe

```bash
# Voir les collections requises par le projet
cat requirements.yml

# Installer toutes les collections déclarées
ansible-galaxy collection install -r requirements.yml
```

**Questions :**
- Où les collections sont-elles installées ? (indice : `ansible.cfg`)
- Quel module de `community.general` utilise-t-on pour le firewall ?

### 5.2 Explorer un rôle de hardening

Explorez la collection `devsec.hardening` :

```bash
# Lister les rôles disponibles dans la collection
ansible-galaxy collection list devsec.hardening

# Regarder les variables du rôle ssh_hardening
# (cherchez dans group_vars/all.yml quelles variables on utilise)
```

**Analysez `group_vars/all/defaults.yml` :**
- Que fait `ssh_server_password_login: false` ?
- Comment `ssh_allow_users` est-elle calculée automatiquement à partir de la liste `users` (regardez le filtre Jinja2) ?
- Que se passerait-il si on inversait l'ordre (hardening avant création des users) ?

### 5.3 Dry-run avec `--check --diff`

```bash
# Simuler l'exécution sans rien modifier (dry-run)
ansible-playbook playbook.yml --check --diff
```

**Comprenez la sortie :**
- Les lignes en **vert** = déjà conforme (idempotent)
- Les lignes en **jaune** = serait modifié
- Les lignes en **rouge** = erreur

### 5.4 Lint du playbook (bonus)

```bash
# Installer ansible-lint
pip install ansible-lint

# Analyser le playbook
ansible-lint playbook.yml
```

Corrigez les éventuels avertissements. Cela enseigne les bonnes pratiques Ansible (nommage, FQCN, idempotence).

---

## 🤖 Test IA

Demandez à une IA :

> *"Écris un playbook Ansible pour installer Podman sur Ubuntu et créer un utilisateur avec une clé SSH"*

**Analysez :**
- L'IA utilise-t-elle les FQCN (`ansible.builtin.apt`, `ansible.posix.authorized_key`) ?
- Les tâches sont-elles idempotentes ?
- L'IA pense-t-elle au hardening SSH (désactiver le login par mot de passe) ?
- Compare-t-elle Podman (rootless) vs Docker (daemon privilégié) ?

**Leçon** : L'IA génère des playbooks fonctionnels mais rarement durcis. La sécurité demande une expertise que les rôles communautaires (`devsec.hardening`) encapsulent.
