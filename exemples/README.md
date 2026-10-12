# Exemples : a quoi ressemblera la suite

Deux scripts facultatifs, a lancer apres le TP1 pour voir ou mene le depot que vous venez d'installer. Ils ne font pas partie des livrables et ne sont pas notes.

## 1. Entrainer un modele (ce que sera la semaine 2)

```
python exemples/train_sentiment.py
```

Le script telecharge 20 000 avis de films en francais (jeu Allocine, 7,6 Mo), decoupe les donnees, entraine un pipeline TF-IDF et regression logistique, affiche le rapport de classification, puis enregistre `models/sentiment.joblib` (environ 19 Mo).

Resultat attendu : une exactitude d'environ 0,915 sur les 4 000 avis de test. Un classifieur lineaire sur des sacs de mots suffit largement pour ce besoin, sans GPU et sans reseau de neurones.

Si le reseau est coupe, le script bascule sur les 30 avis de `data/sample_reviews.csv`. Il tourne alors en une seconde, mais le resultat n'a aucune valeur statistique : six avis en test, une erreur de plus ou de moins deplace le score de 17 points. C'est exactement pourquoi la semaine 2 travaille sur un vrai corpus.

Le modele produit n'entre pas dans Git : `models/*` est exclu par le `.gitignore`, comme tout artefact lourd et reconstructible.

## 2. Afficher une interface (ce que sera la semaine 5)

```
streamlit run exemples/app_streamlit.py
```

Le navigateur s'ouvre sur `http://localhost:8501`. Un onglet analyse un avis saisi a la main, l'autre traite un fichier CSV contenant une colonne `review`.

Lancez d'abord `train_sentiment.py` : sans le modele, l'interface affiche un message d'erreur et s'arrete.

**A observer.** Essayez un avis de film, puis un avis de commerce comme « Livraison rapide, produit conforme ». Mesure obtenue lors de la preparation du kit : « Un film magnifique, j'ai adore » donne positif a 94 %, « Ennuyeux du debut a la fin » donne negatif a 82 %, mais « Livraison rapide, produit conforme » donne negatif a 60 %, donc a tort. Le modele a appris sur des critiques de cinema et ne connait pas ce vocabulaire : c'est le decalage de domaine, etudie au TP2.

## Affichage des accents sous Windows

PowerShell 5.1 lit en ANSI les fichiers UTF-8 et deforme les accents. Pour lire ce fichier correctement :

```
Get-Content exemples\README.md -Encoding UTF8
```

Ou ouvrez-le dans VS Code.

## Source des donnees

Jeu Allocine, publie par T. Blard sous licence MIT : `https://huggingface.co/datasets/tblard/allocine`. Avis publics de spectateurs, aucune donnee personnelle, conforme a la regle du cours sur les donnees.
