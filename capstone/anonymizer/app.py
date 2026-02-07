"""
Anonymizer Service - API Flask pour anonymiser les PII et secrets
Détecte: emails, téléphones, noms ET secrets (API keys, mots de passe, certificats)
"""
from flask import Flask, request, jsonify
import scrubadub
import re

app = Flask(__name__)

# Créer le scrubber avec les détecteurs par défaut
scrubber = scrubadub.Scrubber()

# Patterns de détection de secrets (inspirés de detect-secrets / gitleaks)
SECRET_PATTERNS = {
    'api_key_generic': r'(?i)(api[_-]?key|apikey)\s*[:=]\s*["\']?([a-zA-Z0-9_\-]{20,})["\']?',
    'aws_access_key': r'(?i)AKIA[0-9A-Z]{16}',
    'aws_secret_key': r'(?i)aws[_-]?secret[_-]?access[_-]?key\s*[:=]\s*["\']?([a-zA-Z0-9/+=]{40})["\']?',
    'github_token': r'gh[pousr]_[A-Za-z0-9_]{36,}',
    'openai_key': r'sk-[a-zA-Z0-9]{48,}',
    'anthropic_key': r'sk-ant-[a-zA-Z0-9\-]{40,}',
    'private_key': r'-----BEGIN\s+(RSA\s+)?PRIVATE\s+KEY-----',
    'certificate': r'-----BEGIN\s+CERTIFICATE-----',
    'password_field': r'(?i)(password|passwd|pwd|secret)\s*[:=]\s*["\']?([^\s"\']{8,})["\']?',
    'bearer_token': r'(?i)bearer\s+[a-zA-Z0-9_\-\.]{20,}',
    'jwt_token': r'eyJ[a-zA-Z0-9_-]*\.eyJ[a-zA-Z0-9_-]*\.[a-zA-Z0-9_-]*',
    'connection_string': r'(?i)(mongodb|postgres|mysql|redis)://[^\s]+',
    'slack_webhook': r'https://hooks\.slack\.com/services/[A-Z0-9/]+',
    'stripe_key': r'(?i)(sk|pk)_(test|live)_[a-zA-Z0-9]{24,}',
}


def detect_secrets(text):
    """Détecte les secrets dans le texte et retourne la liste des détections."""
    detections = []
    for secret_type, pattern in SECRET_PATTERNS.items():
        for match in re.finditer(pattern, text):
            detections.append({
                'type': secret_type,
                'text': match.group(0)[:20] + '...' if len(match.group(0)) > 20 else match.group(0),
                'start': match.start(),
                'end': match.end(),
                'full_match': match.group(0)
            })
    return detections


def anonymize_secrets(text):
    """Remplace les secrets détectés par des placeholders."""
    result = text
    for secret_type, pattern in SECRET_PATTERNS.items():
        placeholder = '{{' + secret_type.upper() + '}}'
        result = re.sub(pattern, placeholder, result)
    return result


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy"})


@app.route('/anonymize', methods=['POST'])
def anonymize():
    """
    Anonymise le texte: PII (emails, noms) + Secrets (API keys, passwords).
    
    Input JSON:
        {"text": "Mon email est john@example.com, api_key=sk-abc123..."}
    
    Output JSON:
        {"anonymized": "Mon email est {{EMAIL}}, {{API_KEY_GENERIC}}",
         "pii_count": 1,
         "secrets_count": 1}
    """
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' field"}), 400
    
    original_text = data['text']
    
    # Étape 1: Anonymiser les secrets
    text_no_secrets = anonymize_secrets(original_text)
    secrets_found = detect_secrets(original_text)
    
    # Étape 2: Anonymiser les PII avec Scrubadub
    anonymized_text = scrubber.clean(text_no_secrets)
    pii_found = list(scrubber.iter_filth(text_no_secrets))
    
    return jsonify({
        "anonymized": anonymized_text,
        "original_length": len(original_text),
        "anonymized_length": len(anonymized_text),
        "pii_count": len(pii_found),
        "secrets_count": len(secrets_found)
    })


@app.route('/detect', methods=['POST'])
def detect():
    """
    Détecte les PII et secrets dans le texte sans les remplacer.
    
    Input JSON:
        {"text": "Contact: john@example.com, key: sk-abc123"}
    
    Output JSON:
        {"pii": [...], "secrets": [...]}
    """
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' field"}), 400
    
    text = data['text']
    
    # Détecter PII
    filths = list(scrubber.iter_filth(text))
    pii_detections = [{
        "type": filth.detector_name,
        "text": filth.text,
        "start": filth.beg,
        "end": filth.end
    } for filth in filths]
    
    # Détecter secrets
    secret_detections = detect_secrets(text)
    
    return jsonify({
        "pii": pii_detections,
        "secrets": secret_detections,
        "total_sensitive_items": len(pii_detections) + len(secret_detections)
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
