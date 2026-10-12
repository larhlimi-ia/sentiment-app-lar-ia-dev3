"""Outils partages par les tests du TP1."""
import subprocess
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def root() -> Path:
    """Racine du depot : le dossier qui contient requirements.txt."""
    return Path(__file__).resolve().parent.parent


def dans_un_depot_git(root: Path) -> bool:
    """Vrai si root est dans un arbre de travail Git.

    On interroge Git plutot que de chercher un dossier .git : le projet peut
    etre place dans un sous-dossier d'un depot de regroupement.
    """
    try:
        r = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"],
                           cwd=root, capture_output=True, text=True)
    except FileNotFoundError:
        return False
    return r.returncode == 0 and r.stdout.strip() == "true"


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, capture_output=True,
                          text=True, check=True).stdout
