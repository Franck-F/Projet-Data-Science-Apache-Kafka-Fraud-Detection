"""Configuration du système de logging."""

import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name):
    """Configure et retourne un logger."""
    # Créer le dossier logs s'il n'existe pas
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Configurer le logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Formatter pour les logs
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Handler pour la console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Handler pour le fichier
    file_handler = RotatingFileHandler(
        f"logs/{name}.log",
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
