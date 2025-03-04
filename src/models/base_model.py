from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
import mlflow
import logging
import sys
sys.path.append("../../")
from utils.logger import setup_logger

logger = setup_logger(__name__)

class BaseModel(ABC):
    def __init__(self, model_name):
        self.model_name = model_name
        self.model = None
        
    def prepare_data(self, data: pd.DataFrame, target_col: str):
        """Prépare les données pour l'entraînement."""
        X = data.drop(columns=[target_col])
        y = data[target_col]
        return train_test_split(X, y, test_size=0.2, random_state=42)

    @abstractmethod
    def train(self, X_train, y_train):
        """Entraîne le modèle."""
        pass

    @abstractmethod
    def predict(self, X):
        """Effectue des prédictions."""
        pass

    def evaluate(self, X_test, y_test):
        """Évalue les performances du modèle."""
        try:
            y_pred = self.predict(X_test)
            
            # Calcul des métriques
            report = classification_report(y_test, y_pred)
            auc_roc = roc_auc_score(y_test, y_pred)
            
            # Logging des métriques avec MLflow
            with mlflow.start_run(run_name=self.model_name):
                mlflow.log_metric("auc_roc", auc_roc)
                mlflow.log_params(self.get_params())
                
            logger.info(f"Rapport de classification:\n{report}")
            logger.info(f"AUC-ROC Score: {auc_roc}")
            
            return {
                "classification_report": report,
                "auc_roc": auc_roc
            }
        except Exception as e:
            logger.error(f"Erreur lors de l'évaluation: {str(e)}")
            return None

    @abstractmethod
    def get_params(self):
        """Retourne les paramètres du modèle."""
        pass

    def save_model(self, path):
        """Sauvegarde le modèle."""
        try:
            mlflow.sklearn.save_model(self.model, path)
            logger.info(f"Modèle sauvegardé: {path}")
        except Exception as e:
            logger.error(f"Erreur lors de la sauvegarde du modèle: {str(e)}")

    def load_model(self, path):
        """Charge un modèle sauvegardé."""
        try:
            self.model = mlflow.sklearn.load_model(path)
            logger.info(f"Modèle chargé: {path}")
        except Exception as e:
            logger.error(f"Erreur lors du chargement du modèle: {str(e)}")
