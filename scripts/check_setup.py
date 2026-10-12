#!/usr/bin/env python
"""Diagnostic du poste. Affiche ce qui va et ce qui ne va pas, sans rien modifier.

    python scripts/check_setup.py

Code de sortie 1 s'il reste au moins une erreur.
"""
import importlib
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
erreurs = []
avertissements = []


def ligne(etat: str, texte: str) -> None:
    print(f"  {etat:9} {texte}")


def ok(texte): ligne("OK", texte)
def err(texte):
    ligne("ERREUR", texte); erreurs.append(texte)
def avert(texte):
    ligne("ATTENTION", texte); avertissements.append(texte)


def dans_un_depot_git() -> bool:
    try:
        r = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"],
                           cwd=RACINE, capture_output=True, text=True)
    except FileNotFoundError:
        return False
    return r.returncode == 0 and r.stdout.strip() == "true"


print(f"Diagnostic TP1 dans {RACINE}\n")

print("Python")
v = sys.version_info
(ok if v[:2] == (3, 11) else err)(f"version {v.major}.{v.minor}.{v.micro}"
                                  + ("" if v[:2] == (3, 11) else " : 3.11 attendu"))
(ok if sys.prefix != sys.base_prefix else err)(
    f"environnement virtuel actif ({sys.prefix})" if sys.prefix != sys.base_prefix
    else "environnement virtuel inactif : .venv\\Scripts\\activate")

print("Paquets")
for nom, module in [("pandas", "pandas"), ("scikit-learn", "sklearn"),
                    ("pytest", "pytest"), ("python-dotenv", "dotenv")]:
    try:
        m = importlib.import_module(module)
        ok(f"{nom} {getattr(m, '__version__', '')}".strip())
    except ImportError:
        err(f"{nom} absent : pip install -r requirements.txt")

print("Structure du depot")
for d in ["data", "models", "app", "ui", "tests", "scripts", "docs/cadrage", "exemples"]:
    (ok if (RACINE / d).is_dir() else err)(f"dossier {d}/")
for f in ["README.md", "requirements.txt", ".gitignore", ".gitattributes", ".env.example"]:
    (ok if (RACINE / f).is_file() else err)(f"fichier {f}")
gitignore = (RACINE / ".gitignore").read_text(encoding="utf-8") if (RACINE / ".gitignore").exists() else ""
for regle in [".venv/", "__pycache__/", ".env", "models/*", "mlruns/"]:
    (ok if regle in gitignore else err)(f".gitignore contient {regle}")
(ok if (RACINE / ".env").exists() else avert)(
    "fichier .env cree" if (RACINE / ".env").exists()
    else "fichier .env absent : copy .env.example .env")

print("Git")
if dans_un_depot_git():
    ok("depot Git detecte")
    suivis = subprocess.run(["git", "ls-files"], cwd=RACINE, capture_output=True,
                            text=True).stdout.split()
    (err if ".env" in suivis else ok)(
        ".env suivi par Git : git rm --cached .env" if ".env" in suivis
        else ".env n'est pas suivi par Git")
else:
    avert("ce dossier n'est pas un depot Git : git init ou git clone")

print("Fiches de cadrage")
fiches = sorted((RACINE / "docs" / "cadrage").glob("cas*.md")) if (RACINE / "docs" / "cadrage").is_dir() else []
(ok if len(fiches) == 3 else err)(f"{len(fiches)} fiche(s) trouvee(s)"
                                  + ("" if len(fiches) == 3 else ", 3 attendues"))
for f in fiches:
    n = f.read_text(encoding="utf-8").count("- [x]")
    (ok if n == 1 else avert)(f"{f.name} : {n} approche(s) cochee(s)"
                              + ("" if n == 1 else ", 1 attendue"))

print(f"\nResultat : {len(erreurs)} erreur(s), {len(avertissements)} avertissement(s)")
if erreurs:
    print("Corriger les erreurs avant de pousser.")
sys.exit(1 if erreurs else 0)
