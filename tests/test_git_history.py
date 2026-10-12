"""L'historique Git : au moins un commit par membre du binome, et pas de venv."""
import pytest

from conftest import dans_un_depot_git, git

AUTEURS_MINIMUM = 2


@pytest.fixture(scope="module")
def depot(root):
    if not dans_un_depot_git(root):
        pytest.skip("pas un depot Git : git init ou git clone")
    try:
        git(root, "rev-parse", "HEAD")
    except Exception:
        pytest.skip("aucun commit")
    return root


def test_au_moins_un_commit(depot):
    assert git(depot, "rev-list", "--count", "HEAD").strip() != "0"


def test_un_commit_par_membre(depot):
    sortie = git(depot, "shortlog", "-sn", "--all")
    auteurs = [l.split("\t", 1)[1].strip() for l in sortie.splitlines() if "\t" in l]
    assert len(auteurs) >= AUTEURS_MINIMUM, (
        f"{len(auteurs)} auteur(s) de commits, {AUTEURS_MINIMUM} attendus "
        f"(un par membre du binome) : {auteurs}"
    )


def test_venv_jamais_commite(depot):
    journal = git(depot, "log", "--all", "--name-only", "--pretty=format:")
    assert ".venv/" not in journal, (
        ".venv/ a ete commite au moins une fois : nettoyer l'historique ou refaire le depot"
    )


def test_modele_jamais_commite(depot):
    journal = git(depot, "log", "--all", "--name-only", "--pretty=format:")
    assert ".joblib" not in journal, (
        "un modele .joblib a ete commite : les artefacts lourds restent hors de Git"
    )
