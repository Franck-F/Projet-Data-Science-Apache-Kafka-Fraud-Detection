import pandas as pd
from kafka import KafkaProducer
import json
from datetime import datetime
import logging
import sys
sys.path.append("../../")
from utils.config import KAFKA_CONFIG
from utils.logger import setup_logger

logger = setup_logger(__name__)

class DataCollector:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_CONFIG["bootstrap_servers"],
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        
    def collect_historical_data(self, file_path):
        """Collecte des données historiques depuis un fichier CSV."""
        try:
            df = pd.read_csv(file_path)
            logger.info(f"Données chargées depuis {file_path}: {len(df)} entrées")
            return df
        except Exception as e:
            logger.error(f"Erreur lors du chargement des données: {str(e)}")
            return None

    def send_transaction_to_kafka(self, transaction):
        """Envoie une transaction vers le topic Kafka."""
        try:
            self.producer.send(
                KAFKA_CONFIG["topic_name"],
                value=transaction
            )
            logger.info(f"Transaction envoyée: {transaction['transaction_id']}")
        except Exception as e:
            logger.error(f"Erreur lors de l'envoi de la transaction: {str(e)}")

    def simulate_real_time_transactions(self, sample_data):
        """Simule un flux de transactions en temps réel."""
        for _, transaction in sample_data.iterrows():
            transaction_dict = transaction.to_dict()
            transaction_dict["timestamp"] = datetime.now().isoformat()
            self.send_transaction_to_kafka(transaction_dict)

if __name__ == "__main__":
    collector = DataCollector()
    # Exemple d'utilisation
    historical_data = collector.collect_historical_data("path/to/historical_data.csv")
    if historical_data is not None:
        collector.simulate_real_time_transactions(historical_data)
