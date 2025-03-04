"""Analyse exploratoire des données de transactions."""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def charger_donnees(chemin_fichier):
    """Charge les données depuis un fichier CSV."""
    try:
        df = pd.read_csv(chemin_fichier)
        print(f"Données chargées depuis {chemin_fichier}: {len(df)} entrées")
        return df
    except Exception as e:
        print(f"Erreur lors du chargement des données: {str(e)}")
        return None

def afficher_statistiques_descriptives(df):
    """Affiche les statistiques descriptives des données."""
    print("\nStatistiques descriptives:")
    print(df.describe())
    
    print("\nInformations sur les types de données:")
    print(df.info())
    
    print("\nValeurs manquantes:")
    print(df.isnull().sum())

def visualiser_distribution_transactions(df):
    """Visualise la distribution des transactions normales vs frauduleuses."""
    fig = px.pie(
        df,
        names="is_fraud",
        title="Distribution des transactions frauduleuses vs normales"
    )
    fig.show()

def visualiser_distribution_montants(df):
    """Visualise la distribution des montants par type de transaction."""
    fig = px.box(
        df,
        x="is_fraud",
        y="montant",
        title="Distribution des montants par type de transaction"
    )
    fig.show()

def analyser_patterns_temporels(df):
    """Analyse les patterns temporels des transactions."""
    # Convertir la colonne heure_transaction en datetime si nécessaire
    if not pd.api.types.is_datetime64_any_dtype(df["heure_transaction"]):
        df["heure_transaction"] = pd.to_datetime(df["heure_transaction"])
        
    # Extraire l'heure
    df["hour"] = df["heure_transaction"].dt.hour
    
    fig = px.histogram(
        df,
        x="hour",
        color="is_fraud",
        title="Distribution horaire des transactions"
    )
    fig.show()

def creer_matrice_correlation(df):
    """Génère une matrice de corrélation pour les caractéristiques numériques."""
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
    corr_matrix = df[numeric_cols].corr()
    
    fig = px.imshow(
        corr_matrix,
        title="Matrice de corrélation des caractéristiques"
    )
    fig.show()

def analyser_caracteristiques_importantes(df):
    """Analyse les caractéristiques les plus importantes pour la détection."""
    # Analyse par type de transaction
    print("\nAnalyse par type de transaction:")
    print(df.groupby("type_transaction")["is_fraud"].mean().sort_values(ascending=False))
    
    # Analyse par localisation
    print("\nAnalyse par localisation:")
    print(df.groupby("localisation")["is_fraud"].mean().sort_values(ascending=False))

def sauvegarder_visualisations(df, dossier_sortie="rapports"):
    """Sauvegarde les visualisations dans des fichiers HTML."""
    import os
    if not os.path.exists(dossier_sortie):
        os.makedirs(dossier_sortie)
    
    # Distribution des transactions
    fig = px.pie(df, names="is_fraud", title="Distribution des transactions")
    fig.write_html(f"{dossier_sortie}/distribution_transactions.html")
    
    # Distribution des montants
    fig = px.box(df, x="is_fraud", y="montant", title="Distribution des montants")
    fig.write_html(f"{dossier_sortie}/distribution_montants.html")
    
    # Patterns temporels
    if not pd.api.types.is_datetime64_any_dtype(df["heure_transaction"]):
        df["heure_transaction"] = pd.to_datetime(df["heure_transaction"])
    df["hour"] = df["heure_transaction"].dt.hour
    fig = px.histogram(df, x="hour", color="is_fraud", title="Distribution horaire")
    fig.write_html(f"{dossier_sortie}/patterns_temporels.html")
    
    # Matrice de corrélation
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
    corr_matrix = df[numeric_cols].corr()
    fig = px.imshow(corr_matrix, title="Matrice de corrélation")
    fig.write_html(f"{dossier_sortie}/matrice_correlation.html")

if __name__ == "__main__":
    # Exemple d'utilisation
    chemin_donnees = "data/transactions.csv"
    df = charger_donnees(chemin_donnees)
    
    if df is not None:
        # Afficher les statistiques descriptives
        afficher_statistiques_descriptives(df)
        
        # Créer les visualisations
        visualiser_distribution_transactions(df)
        visualiser_distribution_montants(df)
        analyser_patterns_temporels(df)
        creer_matrice_correlation(df)
        
        # Analyser les caractéristiques importantes
        analyser_caracteristiques_importantes(df)
        
        # Sauvegarder les visualisations
        sauvegarder_visualisations(df)
