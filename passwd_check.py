import re
import sys

RULES = [
    ("min 8 chars", lambda s: len(s) >= 8),
    ("upper", lambda s: re.search(r"[A-Z]", s)),
    ("lower", lambda s: re.search(r"[a-z]", s)),
    ("digit", lambda s: re.search(r"\d", s)),
    ("symbol", lambda s: re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\[\]]", s)),
]

# Vérifie si un mot de passe est fort
def strong(pw: str) -> bool:
    return all(rule(pw) for _, rule in RULES)

if __name__ == "__main__":
    # Liste des mots de passe à tester
    tests = ["azerty", "Password123!", "123456", "StrongPass#2025"]

    for t in tests:
        print(f"{t} -> {'Valide ✅' if strong(t) else 'Invalide ❌'}")

    # Réussir si AU MOINS un mot de passe est valide
    any_ok = any(strong(t) for t in tests)
    sys.exit(0 if any_ok else 1)