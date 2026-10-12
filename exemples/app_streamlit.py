#!/usr/bin/env python
"""Exemple facultatif : ce que sera la semaine 5.

    streamlit run exemples/app_streamlit.py

Lancer d'abord exemples/train_sentiment.py : sans models/sentiment.joblib,
la page affiche un message d'erreur et s'arrete.

Chaque interaction reexecute le script de haut en bas : c'est le modele de
Streamlit. D'ou @st.cache_resource sur le chargement du modele.
"""
from pathlib import Path

import pandas as pd
import streamlit as st

RACINE = Path(__file__).resolve().parent.parent
MODELE = RACINE / "models" / "sentiment.joblib"

st.set_page_config(page_title="Analyse de sentiment", page_icon=":speech_balloon:")


@st.cache_resource
def charger():
    import joblib
    return joblib.load(MODELE)


st.title("Analyse de sentiment des avis clients")
st.caption("Fil rouge du cours : modele entraine en semaine 2, interface en semaine 5.")

if not MODELE.exists():
    st.error("models/sentiment.joblib introuvable.")
    st.info("Lancez d'abord : python exemples/train_sentiment.py")
    st.stop()

modele = charger()
onglet_avis, onglet_fichier = st.tabs(["Un avis", "Un fichier CSV"])

with onglet_avis:
    texte = st.text_area("Avis a analyser", "Livraison rapide, produit conforme.")
    if st.button("Analyser") and texte.strip():
        probas = modele.predict_proba([texte])[0]
        i = probas.argmax()
        label = modele.classes_[i]
        message = f"Avis {'positif' if label == 'positive' else 'negatif'} " \
                  f"(confiance {probas[i]:.0%})"
        (st.success if label == "positive" else st.error)(message)
        st.progress(float(probas[i]))
        if probas[i] < 0.60:
            st.warning("Confiance proche de 50 % : l'avis est peut-etre hors du "
                       "domaine appris par le modele.")

with onglet_fichier:
    fichier = st.file_uploader("Fichier CSV avec une colonne 'review'", type="csv")
    if fichier is not None:
        df = pd.read_csv(fichier)
        if "review" not in df.columns:
            st.error("Colonne 'review' absente du fichier.")
        else:
            df["prediction"] = modele.predict(df["review"].astype(str))
            st.bar_chart(df["prediction"].value_counts())
            st.dataframe(df, width="stretch")
            st.download_button("Telecharger les predictions (CSV)",
                               df.to_csv(index=False).encode("utf-8"),
                               "predictions.csv", "text/csv")
