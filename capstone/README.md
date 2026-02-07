# 🚀 Capstone - Plateforme IA Sécurisée

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

## Services

| Service | Port | Description |
|---------|------|-------------|
| **anonymizer** | 5001 | Masque les PII (emails, téléphones, noms) |
| **litellm** | 8000 | Proxy unifié pour Claude/GPT/Gemini |

## Prérequis

1. **API Keys** (au moins une) :
   - OpenAI : `OPENAI_API_KEY`
   - Anthropic : `ANTHROPIC_API_KEY`
   - Google : `GEMINI_API_KEY`

2. **Docker & Docker Compose**

## Démarrage rapide

```bash
# 1. Copier les variables d'environnement
cp .env.example .env

# 2. Éditer .env avec vos API keys
nano .env

# 3. Lancer les services
docker-compose up -d

# 4. Vérifier
docker-compose ps
```

## Test

### Anonymizer seul

```bash
# Health check
curl http://localhost:5001/health

# Anonymiser du texte
curl -X POST http://localhost:5001/anonymize \
  -H "Content-Type: application/json" \
  -d '{"text": "Contactez john.doe@email.com au 0612345678"}'
```

### LiteLLM seul

```bash
# Liste des modèles
curl http://localhost:8000/v1/models

# Chat completion
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Bonjour!"}]
  }'
```

### Flow complet (Anonymize → LLM)

```bash
# Étape 1: Anonymiser
TEXT="Mon email est jean.dupont@entreprise.fr"
ANON=$(curl -s -X POST http://localhost:5001/anonymize \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"$TEXT\"}" | jq -r '.anonymized')

echo "Texte anonymisé: $ANON"

# Étape 2: Envoyer au LLM
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"gpt-3.5-turbo\",
    \"messages\": [{\"role\": \"user\", \"content\": \"$ANON\"}]
  }"
```

## Nettoyage

```bash
docker-compose down -v
```
