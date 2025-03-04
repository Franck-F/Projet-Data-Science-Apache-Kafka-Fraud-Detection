"""Implémentation du modèle XGBoost pour la détection de fraudes."""

import xgboost as xgb
from base_model import BaseModel
import sys
sys.path.append("../../")
from utils.config import MODEL_PARAMS

class XGBoostModel(BaseModel):
    def __init__(self, params=None):
        super().__init__("XGBoost")
        self.params = params or MODEL_PARAMS["xgboost"]
        
    def train(self, X_train, y_train):
        """Entraîne le modèle XGBoost."""
        self.model = xgb.XGBClassifier(**self.params)
        self.model.fit(X_train, y_train)
        
    def predict(self, X):
        """Effectue des prédictions."""
        return self.model.predict(X)
    
    def predict_proba(self, X):
        """Retourne les probabilités de prédiction."""
        return self.model.predict_proba(X)
    
    def get_params(self):
        """Retourne les paramètres du modèle."""
        return self.params
