# TP1 : marche a suivre, controles T1 a T7

Chaque controle donne la commande et la sortie attendue. Si une sortie differe, arretez-vous : la suite en depend. Commandes ecrites pour PowerShell ; sous Linux et macOS, remplacez `\` par `/` et `.venv\Scripts\activate` par `source .venv/bin/activate`.

## T1 : cloner le depot

L'URL se lit sur la page du depot GitHub, bouton vert **Code**.

```
git clone https://github.com/<organisation-ecole>/sentiment-app-lar-ia-dev.git
cd sentiment-app-lar-ia-dev
```

Variantes : `git clone git@github.com:<organisation-ecole>/sentiment-app-lar-ia-dev.git` en SSH, ou `gh repo clone <organisation-ecole>/sentiment-app-lar-ia-dev`.

Si vous travaillez a partir du fichier `tp1-kit.zip`, decompressez-le puis retirez l'attribut lecture seule : `attrib -R /S *`.

## T2 : creer l'environnement virtuel

```
py -3.11 -m venv .venv
.venv\Scripts\activate
python --version
```

Attendu : l'invite commence par `(.venv)` et la version affiche `3.11.x`. Toute autre version fera echouer l'installation de scikit-learn (voir `DEPANNAGE.md`, panne 2).

## T3 : installer les dependances

```
pip install -r requirements.txt
pip freeze > requirements.lock
```

Attendu : aucune ligne rouge, et `requirements.lock` non vide. Un fichier de 0 octet signifie que l'installation n'a pas eu lieu.

## T4 : configurer

```
copy .env.example .env
```

Ouvrez `.env` et remplacez la valeur de `API_KEY`. Ce fichier reste sur votre poste.

## T5 : diagnostic

```
python scripts/check_setup.py
```

Attendu : `Resultat : 0 erreur(s)`. Un avertissement sur le depot Git est normal si vous avez decompresse le kit au lieu de le cloner.

## T6 : premiers tests

```
python -m pytest -q
```

Attendu a ce stade, si T1 a T5 sont faits et que les deux membres ont commite : **35 passed, 3 failed**, les trois echecs portant sur les fiches de cadrage encore vides.

Avant le commit du second membre, vous lirez **34 passed, 4 failed** : le quatrieme echec est le test qui compte les auteurs. Si vous voyez des `skipped`, votre dossier n'est pas encore un depot Git.

Remplissez ensuite les trois fiches de `docs/cadrage/`, puis relancez : **38 passed**.

## T7 : commiter et pousser

```
git status
git add -A
git status
git commit -m "TP1 : environnement, structure et cadrage"
git push
```

Entre les deux `git status`, verifiez qu'aucune de ces entrees n'apparait : `.venv/`, `.env`, un fichier `.joblib`. L'avertissement sur les fins de ligne est sans consequence.

Le second membre du binome pousse a son tour :

```
git pull
git commit --allow-empty -m "TP1 : relecture du binome"
git push
```

Verification finale :

```
python -m pytest -q
git log --format="%an : %s"
```

Attendu : `38 passed`, et deux auteurs distincts. Sur GitHub, onglet **Actions**, l'integration continue doit passer au vert.

## Facultatif : l'apercu des semaines 2 et 5

```
python exemples/train_sentiment.py
streamlit run exemples/app_streamlit.py
```

Au premier lancement de Streamlit, laissez vide la demande d'adresse de courriel et appuyez sur Entree. Pour arreter : `Ctrl+C`. Details dans `exemples/README.md`.

## Recapitulatif des cibles

| Moment | Attendu |
| --- | --- |
| Kit juste decompresse : ni venv, ni `.env`, ni depot Git | `28 passed, 5 failed, 5 skipped` |
| Venv et `.env` en place, un seul auteur | `34 passed, 4 failed` |
| Deux auteurs, fiches encore vides | `35 passed, 3 failed` |
| Fiches remplies | `38 passed` |

Ces quatre etats ont ete mesures lors de la preparation du kit.
