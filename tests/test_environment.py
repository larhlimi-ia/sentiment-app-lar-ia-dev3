"""L'environnement du poste : version de Python, venv, paquets, secrets."""
import importlib
import sys

import pytest

from conftest import dans_un_depot_git, git

PAQUETS = ["pandas", "sklearn", "pytest", "dotenv"]


def test_version_de_python():
    assert sys.version_info[:2] == (3, 11), (
        f"Python {sys.version_info.major}.{sys.version_info.minor} detecte, 3.11 attendu : "
        "recreez le venv avec py -3.11 -m venv .venv"
    )


def test_environnement_virtuel_actif():
    assert sys.prefix != sys.base_prefix, (
        "pytest ne tourne pas dans le venv : activez-le avec .venv\\Scripts\\activate"
    )


@pytest.mark.parametrize("paquet", PAQUETS)
def test_paquet_installe(paquet):
    importlib.import_module(paquet)


def test_env_example_present(root):
    assert (root / ".env.example").exists(), ".env.example doit rester dans le depot"


def test_env_local_cree(root):
    assert (root / ".env").exists(), "copiez .env.example en .env et changez API_KEY"


def test_env_jamais_suivi_par_git(root):
    if not dans_un_depot_git(root):
        pytest.skip("pas un depot Git")
    suivis = git(root, "ls-files").split()
    assert ".env" not in suivis, ".env est suivi par Git : git rm --cached .env"
    assert not any(p.startswith(".venv/") for p in suivis), ".venv/ est suivi par Git"
