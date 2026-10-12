# sentiment-app : depot du fil rouge

Depot de binome du cours **Developpement et deploiement d'applications intelligentes**. Il accueille, semaine apres semaine, l'application fil rouge : un classifieur de sentiment, son API, son interface et son deploiement.

| Semaine | Ce qui arrive dans ce depot |
| --- | --- |
| 1 | environnement, structure, fiches de cadrage, tests |
| 2 | `src/` : entrainement, evaluation, prediction |
| 3 | `app/` : API FastAPI |
| 5 | `ui/` : interface Streamlit |
| 7 | suivi des experiences et de la derive |
| 8 | conteneur et integration continue |

## Demarrer

```
py -3.11 -m venv .venv          # Windows ; Linux et macOS : python3.11 -m venv .venv
.venv\Scripts\activate          # Linux et macOS : source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env          # Linux et macOS : cp .env.example .env
python scripts/check_setup.py
pytest -q
```

Python **3.11** est obligatoire : les versions plus recentes n'ont pas de roue precompilee pour `scikit-learn 1.5` et tenteraient une compilation depuis les sources.

## Structure

```
data/     donnees ; seul sample_reviews.csv est versionne
models/   artefacts entraines ; jamais versionnes
app/      API (semaine 3)
ui/       interface (semaine 5)
src/      code du modele (semaine 2)
tests/    tests du cours
scripts/  check_setup.py
docs/     cadrage et notes de seance
exemples/ apercu facultatif des semaines 2 et 5
```

## Regles du depot

- `.env` n'est **jamais** commite : il contient la cle d'API. Seul `.env.example` l'est.
- `.venv/` et `models/*.joblib` n'entrent pas dans Git : lourds et reconstructibles.
- Chaque membre du binome pousse au moins un commit : un test le verifie.
- L'integration continue rejoue le diagnostic et les tests a chaque push.

## Documentation

| Fichier | Contenu |
| --- | --- |
| `TP1-ENONCE.md` | enonce de la seance, livrables, bareme |
| `MARCHE-A-SUIVRE.md` | la demarche pas a pas, avec les sorties attendues |
| `TESTS.md` | ce que chaque test verifie et comment lire un echec |
| `DEPANNAGE.md` | les pannes frequentes et leur correction |
| `AIDE-GIT.md` | les commandes Git utiles au binome |
| `exemples/README.md` | les deux scripts d'apercu |
