# Depannage : les pannes rencontrees en seance

Classees dans l'ordre ou elles apparaissent.

## 1. `pytest n'est pas reconnu`

Le venv est actif mais vide : `pip install -r requirements.txt` n'a pas ete lance, ou l'a ete ailleurs. Signe revelateur : `requirements.lock` fait 0 octet.

```
python -c "import sys; print(sys.executable)"   # doit finir par .venv\Scripts\python.exe
pip install -r requirements.txt
python -m pytest -q
```

Preferez toujours `python -m pytest` a `pytest` : la forme module ne depend pas du `PATH`.

## 2. Echec de compilation de scikit-learn

Messages contenant `ninja.exe`, `pip-build-env` et `metadata-generation-failed`.

Le venv n'est pas en Python 3.11. `scikit-learn 1.5` ne fournit des roues precompilees que jusqu'a Python 3.12 ; au-dela, pip tente une compilation depuis les sources, qui echoue sans compilateur C.

```
py --list                          # quelles versions sont installees
winget install Python.Python.3.11  # si 3.11 est absent
deactivate
Remove-Item -Recurse -Force .venv
py -3.11 -m venv .venv
.venv\Scripts\activate
python --version                   # 3.11.x
pip install -r requirements.txt
```

N'assouplissez pas la version dans `requirements.txt` : un test verifie la version de Python.

## 3. `ResolutionImpossible` sur pyarrow

Deux lignes de `requirements.txt` se contredisent. La borne retenue par le cours est `pyarrow==17.0.0`, compatible avec MLflow 2.17 utilise en semaine 7. Si le conflit reapparait, signalez-le plutot que de modifier les versions au hasard.

## 4. Fichiers en lecture seule

Les fichiers extraits d'une archive portent l'attribut lecture seule, ce qui bloque toute modification, y compris par les scripts du kit.

```
attrib -R /S *
```

## 5. L'activation du venv est refusee

PowerShell bloque les scripts. Une fois pour toutes :

```
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Si le message est plutot « Le module .venv n'a pas pu etre charge », c'est que `.venv\Scripts\activate` n'existe pas dans ce dossier : vous n'etes pas a la racine du depot, ou le venv est ailleurs.

## 6. Quatre ou cinq tests `skipped`, « pas un depot Git »

Le kit a ete decompresse au lieu d'etre clone. Les tests Git s'activent des qu'un depot existe :

```
git init
git add -A
git status            # .venv/ ne doit pas apparaitre
git commit -m "init"
```

Le meme message apparait si le projet est place dans un sous-dossier d'un autre depot : les tests interrogent Git, pas la presence d'un dossier `.git`, donc ils fonctionnent aussi dans ce cas.

## 7. Avertissements LF et CRLF au `git add`

```
warning: in the working copy of '...', LF will be replaced by CRLF
```

Simple avertissement, pas une erreur : le `.gitattributes` du kit normalise les fins de ligne pour tout le binome. Les fichiers sont bien ajoutes.

## 8. Accents illisibles dans un fichier `.md`

PowerShell 5.1 lit en ANSI les fichiers UTF-8 sans BOM et affiche `Ã©` a la place de `e` accentue. Le fichier est correct sur le disque.

```
Get-Content <fichier>.md -Encoding UTF8
```

Ou ouvrez le fichier dans VS Code.

## 9. Streamlit demande une adresse de courriel

Ecran d'accueil du premier lancement. Laissez vide et appuyez sur Entree. Le kit desactive deja la collecte de statistiques dans `.streamlit/config.toml`.

## 10. L'interface affiche « modele introuvable »

Lancez d'abord `python exemples/train_sentiment.py`. Le modele n'est pas dans le depot : il est exclu par le `.gitignore` et doit etre reconstruit sur chaque poste.

## 11. Un avis evident est mal classe

Par exemple « Livraison rapide, produit conforme » classe negatif avec 54 % de confiance. Ce n'est pas une panne. Le modele d'exemple a appris sur des critiques de cinema et ne connait pas le vocabulaire du commerce. La confiance proche de 50 % est le signal. C'est le decalage de domaine, etudie au TP2.
