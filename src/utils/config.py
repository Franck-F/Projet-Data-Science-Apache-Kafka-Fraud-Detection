"""Configuration du système de détection de fraudes."""

KAFKA_CONFIG = {
    "bootstrap_servers": "localhost:9092",
    "topic_name": "transactions",
    "fraud_threshold": 0.8,  # Seuil pour considérer une transaction comme frauduleuse
    "group_id": "fraud_detection_group"
}

MLFLOW_CONFIG = {
    "tracking_uri": "http://localhost:5000",
    "experiment_name": "fraud_detection"
}

# Configuration des caractéristiques pour le modèle
FEATURES = [
    "montant",
    "heure_transaction",
    "type_transaction",
    "localisation",
    "device_id",
    "user_id"
]

# Configuration des hyperparamètres par défaut
MODEL_PARAMS = {
    "xgboost": {
        "n_estimators": 100,
        "max_depth": 5,
        "learning_rate": 0.1,
        "objective": "binary:logistic"
    },
    "isolation_forest": {
        "n_estimators": 100,
        "contamination": 0.1,
        "random_state": 42
    }
}
