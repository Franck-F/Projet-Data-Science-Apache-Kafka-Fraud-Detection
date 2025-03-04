from kafka import KafkaConsumer
import json
import mlflow
import pandas as pd
import logging
import sys
sys.path.append("../../")
from utils.config import KAFKA_CONFIG
from utils.logger import setup_logger

logger = setup_logger(__name__)

class FraudDetectionConsumer:
    def __init__(self, model_path):
        self.consumer = KafkaConsumer(
            KAFKA_CONFIG["topic_name"],
            bootstrap_servers=KAFKA_CONFIG["bootstrap_servers"],
            value_deserializer=lambda x: json.loads(x.decode("utf-8"))
        )
        self.model = mlflow.sklearn.load_model(model_path)
        logger.info("Consumer initialisé et modèle chargé")

    def preprocess_transaction(self, transaction):
        """Prétraite une transaction pour la prédiction."""
        try:
            # Convertir la transaction en DataFrame
            df = pd.DataFrame([transaction])
            # Appliquer les mêmes prétraitements que pour l'entraînement
            # TODO: Implémenter la logique de prétraitement
            return df
        except Exception as e:
            logger.error(f"Erreur lors du prétraitement: {str(e)}")
            return None

    def score_transaction(self, transaction):
        """Calcule le score de fraude pour une transaction."""
        try:
            processed_data = self.preprocess_transaction(transaction)
            if processed_data is not None:
                fraud_probability = self.model.predict_proba(processed_data)[0][1]
                return fraud_probability
            return None
        except Exception as e:
            logger.error(f"Erreur lors du scoring: {str(e)}")
            return None

    def process_transactions(self):
        """Traite le flux continu de transactions."""
        logger.info("Démarrage du traitement des transactions")
        for message in self.consumer:
            transaction = message.value
            
            # Score de la transaction
            fraud_score = self.score_transaction(transaction)
            
            if fraud_score is not None:
                # Ajouter le score à la transaction
                transaction["fraud_score"] = fraud_score
                
                # Vérifier si la transaction est suspecte
                if fraud_score > KAFKA_CONFIG["fraud_threshold"]:
                    self.handle_suspicious_transaction(transaction)
                
                logger.info(f"Transaction {transaction['transaction_id']} traitée. Score: {fraud_score}")

    def handle_suspicious_transaction(self, transaction):
        """Gère les transactions suspectes."""
        logger.warning(f"Transaction suspecte détectée: {transaction['transaction_id']}")
        # TODO: Implémenter la logique d'alerte
        # Par exemple: envoi d'email, notification push, etc.

if __name__ == "__main__":
    consumer = FraudDetectionConsumer("path/to/saved_model")
    consumer.process_transactions()
