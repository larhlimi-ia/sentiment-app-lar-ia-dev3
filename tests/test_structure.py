"""La structure du depot : dossiers, fichiers, contenu du .gitignore."""
import pytest

DOSSIERS = ["data", "models", "app", "ui", "tests", "scripts", "docs/cadrage", "exemples"]
FICHIERS = ["README.md", "requirements.txt", ".gitignore", ".gitattributes",
            "pytest.ini", ".env.example"]
EXCLUSIONS = [".venv/", "__pycache__/", ".env", "models/*", "mlruns/"]


@pytest.mark.parametrize("dossier", DOSSIERS)
def test_dossier_present(root, dossier):
    assert (root / dossier).is_dir(), f"dossier manquant : {dossier}"


@pytest.mark.parametrize("fichier", FICHIERS)
def test_fichier_present(root, fichier):
    assert (root / fichier).is_file(), f"fichier manquant : {fichier}"


@pytest.mark.parametrize("regle", EXCLUSIONS)
def test_gitignore_contient(root, regle):
    contenu = (root / ".gitignore").read_text(encoding="utf-8")
    assert regle in contenu, f".gitignore doit contenir {regle}"


def test_echantillon_de_donnees(root):
    import csv
    chemin = root / "data" / "sample_reviews.csv"
    assert chemin.exists(), "data/sample_reviews.csv manquant"
    with chemin.open(encoding="utf-8") as f:
        lignes = list(csv.DictReader(f))
    assert len(lignes) == 30, f"{len(lignes)} avis, 30 attendus"
    assert set(lignes[0]) == {"review", "label"}
    assert {l["label"] for l in lignes} == {"positive", "negative"}
