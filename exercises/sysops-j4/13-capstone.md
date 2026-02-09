# 🎯 Exercice 13 : Plateforme IA Sécurisée (Capstone)

> 🔴 Niveau : Avancé | ⏱️ Durée : 60 min

## Objectif

Déployer une plateforme IA sécurisée utilisant tout ce que vous avez appris :
- **Anonymisation** des données sensibles avant envoi
- **Proxy LLM** pour accès unifié à Claude/GPT/Gemini
- **Infrastructure** Terraform + configuration Ansible

## Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                    Plateforme IA Sécurisée                       │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Utilisateur ──► Anonymizer ──► LiteLLM ──► Claude/GPT/Gemini   │
│                   (Scrubadub)     (Proxy)     (APIs publiques)   │
│                   :5001           :8000                          │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

## Prérequis

- Tous les exercices précédents complétés
- VM cloud disponible (exercice 05)
- Docker, Terraform, Ansible fonctionnels
- **API Key** fournie par le formateur (OpenAI, Anthropic ou Google)

## Instructions

### Étape 1 : Explorer la stack IA (10 min)

1. **Découvrir le dossier capstone**
   ```bash
   cd ~/chemin/vers/denvr/capstone
   ls -la
   ```

2. **Comprendre les composants**

   | Fichier | Rôle |
   |---------|------|
   | `docker-compose.yml` | Orchestre les 2 services |
   | `anonymizer/` | Service Python de masquage PII |
   | `litellm-config.yaml` | Configuration des modèles LLM |
   | `.env.example` | Template pour les API keys |

3. **Analyser l'anonymizer**
   ```bash
   cat anonymizer/app.py
   cat anonymizer/Dockerfile
   ```

   **Questions :**
   - [ ] Quel framework Python est utilisé ?
   - [ ] Quels types de PII sont détectés ?
   - [ ] Le Dockerfile utilise-t-il un multi-stage build ?

### Étape 2 : Tester en local (15 min)

1. **Configurer les API keys**
   ```bash
   cp .env.example .env
   # Éditer .env avec la clé fournie par le formateur
   nano .env
   ```

2. **Lancer la stack**
   ```bash
   docker-compose up -d --build
   docker-compose ps
   ```

3. **Tester l'anonymizer**
   ```bash
   # Health check
   curl http://localhost:5001/health
   
   # Anonymiser du texte
   curl -X POST http://localhost:5001/anonymize \
     -H "Content-Type: application/json" \
     -d '{"text": "Mon email est jean.dupont@entreprise.fr et mon tel 0612345678"}'
   ```

   **Résultat attendu :**
   ```json
   {
     "anonymized": "Mon email est {{EMAIL}} et mon tel {{PHONE}}",
     "original_length": 58,
     "anonymized_length": 42
   }
   ```

4. **Tester LiteLLM**
   ```bash
   # Liste des modèles disponibles
   curl http://localhost:8000/v1/models
   
   # Chat completion
   curl -X POST http://localhost:8000/v1/chat/completions \
     -H "Content-Type: application/json" \
     -d '{
       "model": "gpt-3.5-turbo",
       "messages": [{"role": "user", "content": "Bonjour, qui es-tu?"}]
     }'
   ```

### Étape 3 : Flow complet sécurisé (15 min)

1. **Créer un script de test**
   ```bash
   cat > test-flow.sh << 'EOF'
   #!/bin/bash
   
   # Texte avec des données sensibles
   TEXT="Bonjour, je suis Jean Dupont. Mon email est jean.dupont@entreprise.fr"
   
   echo "📝 Texte original:"
   echo "$TEXT"
   echo ""
   
   # Étape 1: Anonymiser
   echo "🔒 Anonymisation..."
   ANON=$(curl -s -X POST http://localhost:5001/anonymize \
     -H "Content-Type: application/json" \
     -d "{\"text\": \"$TEXT\"}" | jq -r '.anonymized')
   
   echo "Texte anonymisé: $ANON"
   echo ""
   
   # Étape 2: Envoyer au LLM
   echo "🤖 Envoi au LLM..."
   RESPONSE=$(curl -s -X POST http://localhost:8000/v1/chat/completions \
     -H "Content-Type: application/json" \
     -d "{
       \"model\": \"gpt-3.5-turbo\",
       \"messages\": [{\"role\": \"user\", \"content\": \"$ANON\"}]
     }" | jq -r '.choices[0].message.content')
   
   echo "Réponse LLM: $RESPONSE"
   EOF
   
   chmod +x test-flow.sh
   ./test-flow.sh
   ```

2. **Vérifier la protection des données**
   - Le texte envoyé au LLM ne contient-il plus de PII ?
   - Les données sensibles restent-elles sur votre infrastructure ?

### Étape 4 : Déployer sur le cloud (20 min)

1. **Préparer le déploiement Ansible**
   ```bash
   # Créer un playbook pour déployer la stack IA
   cat > deploy-ai-platform.yml << 'EOF'
   ---
   - name: Deploy AI Platform
     hosts: webservers
     become: true
     vars:
       app_dir: /opt/ai-platform
     
     tasks:
       - name: Create app directory
         ansible.builtin.file:
           path: "{{ app_dir }}"
           state: directory
           mode: '0755'
       
       - name: Copy docker-compose files
         ansible.builtin.copy:
           src: "{{ item }}"
           dest: "{{ app_dir }}/"
         loop:
           - docker-compose.yml
           - litellm-config.yaml
           - .env
       
       - name: Copy anonymizer folder
         ansible.builtin.copy:
           src: anonymizer/
           dest: "{{ app_dir }}/anonymizer/"
       
       - name: Start services
         community.docker.docker_compose:
           project_src: "{{ app_dir }}"
           state: present
           build: true
   EOF
   ```

2. **Déployer**
   ```bash
   ansible-playbook -i inventory deploy-ai-platform.yml
   ```

3. **Tester depuis le cloud**
   ```bash
   curl http://VM_IP:5001/health
   curl http://VM_IP:8000/v1/models
   ```

---

## 🧪 Validation

✅ Vous avez réussi si :
- [ ] L'anonymizer masque correctement les emails et téléphones
- [ ] LiteLLM répond aux requêtes chat
- [ ] Le flow complet (anonymize → LLM) fonctionne
- [ ] La stack est déployée sur le cloud

---

## 💡 Troubleshooting

| Problème | Solution |
|----------|----------|
| `anonymizer` ne démarre pas | Vérifier `docker-compose logs anonymizer` |
| LiteLLM erreur 401 | Vérifier les API keys dans `.env` |
| Requête timeout | API key invalide ou quota dépassé |
| Port déjà utilisé | `docker-compose down` puis relancer |

---

## ✅ Solution

<details>
<summary>Commandes complètes</summary>

```bash
cd capstone

# Configuration
cp .env.example .env
# Éditer .env

# Lancement
docker-compose up -d --build

# Tests
curl http://localhost:5001/health
curl -X POST http://localhost:5001/anonymize \
  -H "Content-Type: application/json" \
  -d '{"text": "Email: test@example.com"}'

curl http://localhost:8000/v1/models
```

</details>

---

## 🤖 Réflexion finale

À la fin de cet exercice, réfléchissez :

> *"Pourquoi anonymiser les données avant de les envoyer à un LLM externe ?"*

**Raisons :**
1. **RGPD** : Les données personnelles ne doivent pas quitter l'UE sans garanties
2. **Confidentialité** : Les LLMs peuvent mémoriser les données d'entraînement
3. **Sécurité** : Réduire la surface d'attaque en cas de breach chez le provider
4. **Conformité** : Exigences internes de l'entreprise

**Ce que vous avez appris :**
- ✅ Construire un service de protection des données
- ✅ Utiliser un proxy pour unifier l'accès aux LLMs
- ✅ Déployer une stack complète avec Docker Compose
- ✅ Sécuriser une infrastructure DevSecOps

---

## 🎓 Félicitations !

Vous avez complété le workshop DevSecOps et déployé votre propre plateforme IA sécurisée !

**Prochaines étapes suggérées :**
- [ ] Ajouter une UI web (Open WebUI)
- [ ] Implémenter le logging des requêtes
- [ ] Ajouter de l'authentification (API keys)
- [ ] Explorer d'autres détecteurs Scrubadub (noms, adresses)
