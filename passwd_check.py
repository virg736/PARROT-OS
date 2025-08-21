# passwd_check.py
import re
import sys

# Règles de sécurité pour un mot de passe fort
RULES = [
    ("min 8 chars", lambda s: len(s) >= 8),
    ("upper", lambda s: re.search(r"[A-Z]", s)),
    ("lower", lambda s: re.search(r"[a-z]", s)),
    ("digit", lambda s: re.search(r"\d", s)),
    ("symbol", lambda s: re.search(r"[!@#$%^&*(),.?\":{}|<>]", s)),
]

# Vérifie si un mot de passe est fort
def strong(pw: str) -> bool:
    return all(rule(pw) for _, rule in RULES)

if __name__ == "__main__":
    # Liste des mots de passe à tester
    tests = ["azerty", "Password123!", "123456", "StrongPass#2025"]

    ok = True
    for t in tests:
        print(f"{t} -> {'Valide ✅' if strong(t) else 'Invalide ❌'}")
        ok &= strong(t)

    # Retourne 0 si tout est bon, 1 sinon (utile pour GitHub Actions)
    sys.exit(0 if ok else 1)
