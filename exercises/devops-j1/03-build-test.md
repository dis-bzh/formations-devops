# 🎯 Exercice 03 - Build & Test Automatisé

> **Objectif** : Créer un pipeline qui build et teste une application automatiquement

## 📋 Contexte

Vous avez créé votre premier workflow. Maintenant, on va le rendre utile : automatiser le build et les tests de notre future application.

## 🎯 Mission

Créer un workflow GitHub Actions qui :
1. Se déclenche sur chaque `push` et `pull_request`
2. Installe les dépendances
3. Execute les tests
4. Affiche un résumé

## 📝 Instructions

### Étape 1 : Créer l'application de test

Créez un fichier `app.py` :

```python
def hello(name: str = "World") -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    print(hello())
```

### Étape 2 : Créer les tests

Créez un fichier `test_app.py` :

```python
from app import hello, add

def test_hello_default():
    assert hello() == "Hello, World!"

def test_hello_name():
    assert hello("DevOps") == "Hello, DevOps!"

def test_add():
    assert add(2, 3) == 5
```

### Étape 3 : Créer le workflow

Créez `.github/workflows/test.yml` :

```yaml
name: Test

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install pytest
        run: pip install pytest
      
      - name: Run tests
        run: pytest -v
```

### Étape 4 : Push et observer

```bash
git add .
git commit -m "Add CI tests"
git push
```

## ✅ Critères de succès

- [ ] Le workflow se déclenche automatiquement
- [ ] Les 3 tests passent au vert
- [ ] Vous comprenez chaque étape du workflow

## 🔗 Lien avec le Capstone

Ce workflow servira de base pour tester la Secure AI Platform. On ajoutera des tests de sécurité au Jour 4 !

## 📚 Ressources

- [GitHub Actions - Python](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python)
- [pytest documentation](https://docs.pytest.org/)
