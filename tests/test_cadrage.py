"""Les trois fiches de cadrage : rubriques remplies, une approche, deux criteres."""
import re
from pathlib import Path

import pytest

FICHES = ["cas1-pharmacie.md", "cas2-reglement.md", "cas3-avis-negatifs.md"]
RUBRIQUES = ["Besoin en une phrase", "Utilisateur final", "Approche retenue",
             "Justification", "Donnees necessaires", "Metrique de succes",
             "Consequence d'une erreur", "Risques ethiques"]
CRITERES = ["(a)", "(b)", "(c)", "(d)"]
MINIMUM = 20


def corps(texte: str, titre: str) -> str:
    """Texte d'une rubrique, hors lignes de consigne et cases a cocher."""
    motif = re.compile(rf"^##+\s*{re.escape(titre)}.*?$(.*?)(?=^##\s|\Z)",
                       re.MULTILINE | re.DOTALL)
    m = motif.search(texte)
    if not m:
        return ""
    return "\n".join(l for l in m.group(1).splitlines()
                     if l.strip() and not l.startswith(">") and not l.startswith("- ["))


@pytest.fixture(scope="module")
def fiches(root) -> dict[str, str]:
    dossier: Path = root / "docs" / "cadrage"
    trouvees = {}
    for nom in FICHES:
        chemin = dossier / nom
        if not chemin.exists():
            pytest.skip(f"{nom} absent de docs/cadrage/")
        trouvees[nom] = chemin.read_text(encoding="utf-8")
    return trouvees


def test_les_trois_fiches_existent(fiches):
    assert set(fiches) == set(FICHES)


def test_rubriques_remplies(fiches):
    vides = [f"{nom} / {titre}"
             for nom, texte in fiches.items()
             for titre in RUBRIQUES if titre != "Approche retenue"
             if len(corps(texte, titre)) < MINIMUM]
    assert not vides, "rubriques vides ou trop courtes : " + ", ".join(vides)


def test_une_seule_approche_cochee(fiches):
    for nom, texte in fiches.items():
        assert texte.count("- [x]") == 1, f"{nom} : cocher exactement une approche"


def test_justification_cite_deux_criteres(fiches):
    for nom, texte in fiches.items():
        cites = [c for c in CRITERES if c in corps(texte, "Justification")]
        assert len(cites) >= 2, (
            f"{nom} : la justification doit citer au moins deux criteres parmi "
            "(a), (b), (c), (d)"
        )


def test_titre_personnalise(fiches):
    for nom, texte in fiches.items():
        premiere = texte.splitlines()[0]
        assert "<nom du cas>" not in premiere, (
            f"{nom} : remplacez <nom du cas> par le titre du cas dans le titre"
        )
