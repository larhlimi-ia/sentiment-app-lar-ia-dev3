# Ce que verifient les 38 tests

`pytest -q` depuis la racine du depot, venv actif.

## tests/test_environment.py (9 tests)

| Test | Verifie | En cas d'echec |
| --- | --- | --- |
| `test_version_de_python` | Python 3.11 exactement | recreez le venv : `py -3.11 -m venv .venv` |
| `test_environnement_virtuel_actif` | pytest tourne dans le venv | `.venv\Scripts\activate` |
| `test_paquet_installe` (4) | pandas, scikit-learn, pytest, python-dotenv importables | `pip install -r requirements.txt` |
| `test_env_example_present` | `.env.example` est dans le depot | ne le supprimez pas |
| `test_env_local_cree` | `.env` existe sur le poste | `copy .env.example .env` |
| `test_env_jamais_suivi_par_git` | ni `.env` ni `.venv/` suivis par Git | `git rm --cached .env` |

## tests/test_structure.py (20 tests)

Huit dossiers, six fichiers, cinq regles du `.gitignore`, et le contenu de `data/sample_reviews.csv` (30 avis, deux colonnes, deux etiquettes).

## tests/test_cadrage.py (5 tests)

| Test | Verifie |
| --- | --- |
| `test_les_trois_fiches_existent` | les trois fiches sont dans `docs/cadrage/` |
| `test_rubriques_remplies` | chaque rubrique obligatoire fait au moins 20 caracteres, hors lignes `>` et cases a cocher |
| `test_une_seule_approche_cochee` | exactement une case `- [x]` par fiche |
| `test_justification_cite_deux_criteres` | au moins deux marqueurs parmi `(a)`, `(b)`, `(c)`, `(d)` |
| `test_titre_personnalise` | `<nom du cas>` a ete remplace dans le titre |

## tests/test_git_history.py (4 tests)

Au moins un commit, au moins deux auteurs, et ni `.venv/` ni `.joblib` dans tout l'historique.

Ces quatre tests, plus `test_env_jamais_suivi_par_git`, sont **ignores** si le dossier n'est pas dans un depot Git : c'est le cas d'un kit simplement decompresse. Ils s'activent des le `git init` ou le `git clone`.

## Lire un resultat

| Resultat | Etat du poste |
| --- | --- |
| `28 passed, 5 failed, 5 skipped` | kit juste decompresse : ni venv, ni `.env`, ni depot Git |
| `34 passed, 4 failed` | venv et `.env` en place, un seul auteur de commits, fiches vides |
| `35 passed, 3 failed` | deux auteurs, fiches de cadrage encore vides |
| `38 passed` | tout est en place |

Un `skipped` n'est pas un echec : le test indique ce qui lui manque dans son message. Ces quatre etats ont ete mesures lors de la preparation du kit.
