#!/usr/bin/env python
"""Exemple facultatif : ce que sera la semaine 2.

Jeu de donnees : Allocine (tblard/allocine), 20 000 avis du split de validation,
telecharges depuis une URL publique. Licence MIT, avis publics de spectateurs.

    python exemples/train_sentiment.py

Quatre points de methode a reperer dans le code :
  - le decoupage se fait AVANT la vectorisation, sinon le jeu de test fuite ;
  - le Pipeline enferme vectoriseur et modele dans un seul objet ;
  - random_state rend le decoupage reproductible ;
  - c'est le pipeline entier qui est sauvegarde, pas seulement le classifieur.
"""
import sys
from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

RACINE = Path(__file__).resolve().parent.parent
URL = ("https://huggingface.co/datasets/tblard/allocine/resolve/main/"
       "allocine/validation-00000-of-00001.parquet")
SECOURS = RACINE / "data" / "sample_reviews.csv"   # si le reseau est coupe
SORTIE = RACINE / "models" / "sentiment.joblib"
GRAINE = 42


def charger() -> tuple[pd.DataFrame, str]:
    try:
        print("Telechargement des avis Allocine (7,6 Mo, quelques secondes)...")
        brut = pd.read_parquet(URL)
        df = pd.DataFrame({
            "review": brut["review"].astype(str),
            "label": brut["label"].map({0: "negative", 1: "positive"}),
        })
        return df, f"Allocine ({len(df)} avis)"
    except Exception as erreur:
        print(f"Telechargement impossible ({type(erreur).__name__}), "
              "bascule sur data/sample_reviews.csv")
        df = pd.read_csv(SECOURS)
        return df, f"echantillon de secours ({len(df)} avis)"


def main() -> int:
    df, source = charger()
    X_train, X_test, y_train, y_test = train_test_split(
        df["review"], df["label"], test_size=0.2,
        random_state=GRAINE, stratify=df["label"])

    pipe = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)),
        ("clf", LogisticRegression(solver="liblinear", random_state=GRAINE)),
    ])
    pipe.fit(X_train, y_train)

    print(f"\nSource : {source}, {len(X_test)} avis en test\n")
    print(classification_report(y_test, pipe.predict(X_test), digits=3))

    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipe, SORTIE)
    print(f"Modele enregistre : models/sentiment.joblib")
    print("Il n'entre pas dans Git : models/* est exclu par le .gitignore.")
    if "secours" in source:
        print("\nAttention : 30 avis, 6 en test. Le score n'a aucune valeur "
              "statistique. C'est pourquoi la semaine 2 travaille sur un vrai corpus.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
