"""Implémentation du modèle Isolation Forest pour la détection d'anomalies."""

from sklearn.ensemble import IsolationForest
from base_model import BaseModel
import numpy as np
import sys
sys.path.append("../../")
from utils.config import MODEL_PARAMS

class IsolationForestModel(BaseModel):
    def __init__(self, params=None):
        super().__init__("IsolationForest")
        self.params = params or MODEL_PARAMS["isolation_forest"]
        
    def train(self, X_train, y_train=None):
        """Entraîne le modèle Isolation Forest."""
        self.model = IsolationForest(**self.params)
        self.model.fit(X_train)
        
    def predict(self, X):
        """Effectue des prédictions.
        Retourne 1 pour normal, -1 pour anomalie."""
        return self.model.predict(X)
    
    def predict_proba(self, X):
        """Convertit les scores de décision en pseudo-probabilités."""
        scores = self.model.score_samples(X)
        # Normaliser les scores entre 0 et 1
        proba = 1 - (scores - np.min(scores)) / (np.max(scores) - np.min(scores))
        return np.column_stack((1-proba, proba))
    
    def get_params(self):
        """Retourne les paramètres du modèle."""
        return self.params
