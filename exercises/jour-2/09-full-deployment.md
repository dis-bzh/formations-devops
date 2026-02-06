# 🎯 Exercice 09 : Full Deployment (Capstone)

> 🔴 Niveau : Avancé | ⏱️ Durée : 45 min

## Objectif

Déployer l'application complète en utilisant tout ce que vous avez appris.

## Prérequis

- Tous les exercices précédents complétés
- VM cloud disponible (exercice 05)
- Docker, Terraform, Ansible fonctionnels

## Instructions

### Vue d'ensemble

```
┌─────────────────────────────────────────────────────────────────┐
│                        Pipeline Complet                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Build    ──►  2. Push     ──►  3. Deploy   ──►  4. Verify  │
│  (Docker)        (Registry)       (Ansible)        (Test)      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Étape 1 : Build de l'image (10 min)

1. **Construire l'image localement**
   ```bash
   cd ~/chemin/vers/denvr
   
   docker build -t formation-app:v1 .
   ```

2. **Tester localement**
   ```bash
   docker run -d -p 8080:80 --name test-app formation-app:v1
   curl http://localhost:8080
   docker stop test-app && docker rm test-app
   ```

### Étape 2 : Push vers un registry (10 min)

**Option A : GitHub Container Registry (ghcr.io)**

```bash
# Se connecter
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin

# Taguer
docker tag formation-app:v1 ghcr.io/USERNAME/formation-app:v1

# Pousser
docker push ghcr.io/USERNAME/formation-app:v1
```

**Option B : Docker Hub**

```bash
# Se connecter
docker login

# Taguer et pousser
docker tag formation-app:v1 USERNAME/formation-app:v1
docker push USERNAME/formation-app:v1
```

### Étape 3 : Préparer le déploiement (10 min)

1. **Créer un inventory pour votre VM**
   ```bash
   cat > inventory << EOF
   [webservers]
   VM_IP ansible_user=VOTRE_USER ansible_ssh_private_key_file=~/.ssh/votre_cle
   EOF
   ```

2. **Créer un playbook de déploiement**
   ```bash
   cat > deploy-playbook.yml << 'EOF'
   ---
   - name: Deploy containerized app
     hosts: webservers
     become: true
     vars:
       image_name: "ghcr.io/USERNAME/formation-app:v1"
       container_name: "formation-app"
       host_port: 80
       container_port: 80
     
     tasks:
       - name: Docker is installed
         ansible.builtin.apt:
           name: docker.io
           state: present
           update_cache: true

       - name: Docker service started
         ansible.builtin.service:
           name: docker
           state: started
           enabled: true

       - name: Pull the image
         community.docker.docker_image:
           name: "{{ image_name }}"
           source: pull

       - name: Remove old container if exists
         community.docker.docker_container:
           name: "{{ container_name }}"
           state: absent

       - name: Run the container
         community.docker.docker_container:
           name: "{{ container_name }}"
           image: "{{ image_name }}"
           ports:
             - "{{ host_port }}:{{ container_port }}"
           restart_policy: unless-stopped
           state: started
   EOF
   ```

### Étape 4 : Déployer (10 min)

1. **Tester la connexion**
   ```bash
   ansible -i inventory webservers -m ping
   ```

2. **Exécuter le déploiement**
   ```bash
   ansible-playbook -i inventory deploy-playbook.yml
   ```

3. **Vérifier**
   ```bash
   curl http://VM_IP
   ```

### Étape 5 : Vérification et nettoyage (5 min)

1. **Vérifier l'état du conteneur**
   ```bash
   ssh USER@VM_IP "docker ps"
   ```

2. **Voir les logs**
   ```bash
   ssh USER@VM_IP "docker logs formation-app"
   ```

3. **Nettoyage (optionnel)**
   ```bash
   ansible-playbook -i inventory deploy-playbook.yml --tags cleanup
   # Ou manuellement :
   ssh USER@VM_IP "docker stop formation-app && docker rm formation-app"
   ```

---

## 🧪 Validation

✅ Vous avez réussi si :
- [ ] L'image est buildée localement
- [ ] L'image est pushée sur un registry
- [ ] Le playbook Ansible s'exécute sans erreur
- [ ] L'application est accessible via l'IP de la VM
- [ ] Vous avez nettoyé les ressources cloud

---

## 💡 Troubleshooting

| Problème | Solution |
|----------|----------|
| `Permission denied (publickey)` | Vérifier le chemin de la clé SSH |
| `Connection refused` port 80 | Firewall bloque le port ? |
| `Cannot pull image` | Registry privé ? Token expiré ? |
| `Container exits immediately` | `docker logs` pour voir l'erreur |

---

## ✅ Solution

<details>
<summary>Checklist de déploiement</summary>

**Build:**
```bash
docker build -t formation-app:v1 .
docker run -d -p 8080:80 --name test formation-app:v1
curl localhost:8080  # Doit répondre
docker stop test && docker rm test
```

**Push:**
```bash
export GITHUB_TOKEN="ghp_xxx"
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin
docker tag formation-app:v1 ghcr.io/USERNAME/formation-app:v1
docker push ghcr.io/USERNAME/formation-app:v1
```

**Deploy:**
```bash
ansible-playbook -i inventory deploy-playbook.yml
curl http://VM_IP
```

</details>

---

## 🤖 Test IA

À la fin de cet exercice, réfléchissez :

> *"Si j'avais demandé à l'IA de faire tout ça pour moi, aurait-elle réussi ?"*

**Points où l'IA aurait eu du mal :**
- Connaître votre IP de VM, username, clé SSH
- Savoir quel registry vous utilisez
- Debugger une erreur de connexion spécifique à votre environnement
- Gérer les credentials de manière sécurisée

**Ce que vous avez appris qui vous permet de vérifier l'IA :**
- La structure d'un Dockerfile multi-stage
- Le workflow CI/CD (build → push → deploy)
- Les playbooks Ansible et l'idempotence
- Les scans de sécurité

---

## 🎓 Félicitations !

Vous avez complété le workshop DevSecOps !

**Compétences acquises :**
- ✅ Conteneurisation avec Docker
- ✅ CI/CD avec GitHub Actions
- ✅ Infrastructure as Code avec Terraform
- ✅ Configuration Management avec Ansible
- ✅ Security Scanning
- ✅ Pensée critique face à l'IA

**Prochaines étapes suggérées :**
- [ ] Explorer Kubernetes
- [ ] Approfondir GitOps (Flux/ArgoCD)
- [ ] Passer une certification cloud (AZ-900, AWS CCP)
