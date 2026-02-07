# Anonymizer Service

Service Python utilisant Scrubadub pour anonymiser les données sensibles (PII) avant envoi au LLM.

## Usage

```bash
docker-compose up -d
curl -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{"text": "Mon email est john@example.com"}'
```
