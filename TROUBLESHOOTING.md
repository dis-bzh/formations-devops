# 🔧 Troubleshooting - Erreurs Courantes

Guide de résolution des problèmes fréquemment rencontrés.

## Docker

### 🔴 `docker: Cannot connect to the Docker daemon`

**Symptôme :**
```
docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock
```

**Causes possibles :**
1. Docker n'est pas démarré
2. Permissions insuffisantes

**Solutions :**
```bash
# Démarrer Docker
sudo systemctl start docker

# Ajouter l'utilisateur au groupe docker
sudo usermod -aG docker $USER
# Puis déconnexion/reconnexion
```

---

### 🔴 `port is already allocated`

**Symptôme :**
```
Error response from daemon: driver failed programming external connectivity: 
Bind for 0.0.0.0:8080 failed: port is already allocated
```

**Solution :**
```bash
# Trouver ce qui utilise le port
lsof -i :8080
# ou
docker ps  # Un autre conteneur utilise peut-être ce port

# Utiliser un autre port
docker run -p 8081:80 mon-image
```

---

### 🔴 `COPY failed: file not found in build context`

**Symptôme :**
```
COPY failed: file not found in build context or excluded by .dockerignore
```

**Causes :**
1. Le fichier n'existe pas
2. Exclu par `.dockerignore`
3. Chemin relatif incorrect

**Vérifications :**
```bash
# Vérifier que le fichier existe
ls -la fichier

# Vérifier .dockerignore
cat .dockerignore

# Le contexte de build est le dossier où vous lancez docker build
```

---

## Terraform

### 🔴 `Error acquiring the state lock`

**Symptôme :**
```
Error acquiring the state lock
```

**Cause :** Un autre process Terraform tourne ou a crashé.

**Solution :**
```bash
# Forcer le déblocage (avec précaution !)
terraform force-unlock LOCK_ID
```

---

### 🔴 `Provider not found`

**Symptôme :**
```
Error: Failed to query available provider packages
```

**Solution :**
```bash
# Réinitialiser
rm -rf .terraform
terraform init
```

---

## Ansible

### 🔴 `Permission denied (publickey)`

**Symptôme :**
```
fatal: [host]: UNREACHABLE! => {"msg": "Permission denied (publickey,password)"}
```

**Vérifications :**
```bash
# Tester la connexion SSH manuellement
ssh -i ~/.ssh/votre_cle user@host

# Vérifier les permissions de la clé
chmod 600 ~/.ssh/votre_cle

# Vérifier que la clé publique est sur le serveur
cat ~/.ssh/votre_cle.pub
# Doit être dans ~/.ssh/authorized_keys du serveur distant
```

---

### 🔴 `sudo: a password is required`

**Symptôme :**
```
fatal: [host]: FAILED! => {"msg": "Missing sudo password"}
```

**Solutions :**
```bash
# Ajouter --ask-become-pass (demande le mot de passe)
ansible-playbook playbook.yml --ask-become-pass

# OU configurer sudo sans mot de passe sur le serveur
echo "username ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/username
```

---

## GitHub Actions

### 🔴 Workflow ne se déclenche pas

**Vérifications :**
1. Le fichier est-il dans `.github/workflows/` ?
2. Le YAML est-il valide ?
3. Le trigger correspond-il ? (branch, tag, event)

```yaml
# Exemple : déclencher sur main ET develop
on:
  push:
    branches: [main, develop]
```

---

### 🔴 `Resource not accessible by integration`

**Cause :** Permissions insuffisantes.

**Solution :** Vérifier les permissions du `GITHUB_TOKEN` :
```yaml
permissions:
  contents: read
  packages: write
```

---

## Cloud / SSH

### 🔴 `Connection timed out`

**Causes possibles :**
1. VM éteinte
2. IP incorrecte
3. Firewall bloque le port 22

**Vérifications :**
```bash
# Vérifier que la VM tourne
az vm show -d -g RESOURCE_GROUP -n VM_NAME --query powerState

# Vérifier les règles firewall
az network nsg rule list -g RESOURCE_GROUP --nsg-name NSG_NAME
```

---

## 🤖 Ce que l'IA pourrait manquer

| Erreur | Ce que l'IA suggère souvent | Ce qu'il faut vraiment vérifier |
|--------|----------------------------|---------------------------------|
| Permission denied | "Utiliser sudo" | Les permissions du fichier, le groupe docker |
| Port already in use | "Changer de port" | Quel process utilise le port, le tuer si nécessaire |
| Connection timeout | "Vérifier le firewall" | L'IP est-elle correcte ? La VM tourne-t-elle ? |
| State lock | "force-unlock" | Y a-t-il vraiment un conflit ou un process en cours ? |
