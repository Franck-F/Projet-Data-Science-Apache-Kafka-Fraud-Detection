# Projet-Data-Science-Apache-Kafka-Fraud-Detection
Système de détection d'anomalies en temps réel pour identifier les transactions frauduleuses dans un flux de données financières, en utilisant des techniques de Machine Learning.

### À propos du projet
Une grandes banque en ligne pour améliorer sa réactivité face aux transactions frauduleuses afin de servir au mieux ses clients souhaite donc détecter en temps réel les transactions frauduleuses qui pourraient survenir sur les comptes de ses clients.

Dans son système, il enregistre toutes les transactions dans une base de données. Après réflexions au sein de l'équipe technique, l'entreprise a décidé d'utiliser Apache Kafka pour y stocker toutes les transactions financières en temps réel de ses clients. Elle souhaite donc pouvoir utiliser ce système afin d'effectuer des analyses en temps réel et faire remonter les potentielles transactions frauduleuses.

Il sera question dans le rôle de data scientist de mettre en place un consumer qui puisse analyser toutes les transactions en temps réel et faire remonter les transactions potentiellement frauduleuses. Afin d'aider à calibrer un modèle de Machine Learning qui puisse identifier les transactions frauduleuses, l'entreprise utilise des robots qui ajoutent artificiellement des fraudes dans les données.

### Étapes du projet
 - [x] Construire le consumer pour analyser les transactions
 - [x] Calibrer un modèle de régression logistique
 - [x] Détecter en temps réel les cas de fraude
 - [x] Déployer le consumer dans le Cloud
 - [x] Publier le code source et les résultats sur GitHub

### Structure du projet
```
Projet-Data-Science-Apache-Kafka-Fraud-Detection/
├── src/
│   ├── data/
│   │   ├── data_collector.py
│   │   └── data_preprocessor.py
│   ├── models/
│   │   ├── base_model.py
│   │   ├── isolation_forest.py
│   │   └── xgboost_model.py
│   ├── kafka/
│   │   ├── producer.py
│   │   └── consumer.py
│   └── utils/
│       ├── config.py
│       └── logger.py
├── notebooks/
│   └── exploratory_analysis.ipynb
├── tests/
├── config/
├── requirements.txt
└── README.md
```


### Pré-requis
Le projet nécessite Python 3 d'installé sur le système.

>[!NOTE]Installation
> Cloner le projet Git.

> git clone [https://github.com/Franck-F/Projet-Data-Science-Apache-Kafka-Fraud-Detection.git]
> Installer les dépendances du fichier requirements.txt dans un environnement virtuel.

### Installation
1. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Configurer Kafka :
- Installer Apache Kafka
- Démarrer le serveur Zookeeper
- Démarrer le serveur Kafka

4. Configurer MLflow (optionnel) :
```bash
mlflow server --host 0.0.0.0 --port 5000
```

## Utilisation
Le système peut être utilisé en deux modes : entraînement et service.

### Mode Entraînement
Pour entraîner les modèles sur vos données :
```bash
python main.py --mode train --data path/to/your/data.csv
```

Cela va :
1. Charger et analyser vos données
2. Générer des visualisations dans le dossier `reports/`
3. Entraîner les modèles XGBoost et Isolation Forest
4. Sauvegarder les modèles dans le dossier `models/`
5. Logger les métriques dans MLflow

### Mode Service
Pour démarrer le système de détection en temps réel :
```bash
python main.py --mode serve --model models/xgboost_model
```

Cela va :
1. Charger le modèle spécifié
2. Démarrer le consumer Kafka
3. Analyser les transactions en temps réel
4. Générer des alertes pour les transactions suspectes

## Composants Principaux

### Collecte de Données (`data_collector.py`)
- Intégration avec Kafka pour la collecte en temps réel
- Gestion des données historiques
- Simulation de transactions pour les tests

### Modèles (`models/`)
- `base_model.py` : Classe de base pour tous les modèles
- `xgboost_model.py` : Implémentation XGBoost pour l'apprentissage supervisé
- `isolation_forest_model.py` : Implémentation Isolation Forest pour la détection d'anomalies

### Analyse (`analysis/`)
- Analyse exploratoire des données
- Visualisations interactives avec Plotly
- Génération de rapports automatiques

### Traitement en Temps Réel (`consumer.py`)
- Consumer Kafka pour le traitement des transactions
- Scoring en temps réel
- Système d'alertes pour les transactions suspectes

## Tests
```bash
pytest tests/
```

## Monitoring
Le système utilise MLflow pour le suivi des expériences. Vous pouvez accéder à l'interface web MLflow à l'adresse : http://localhost:5000

## Logs
Les logs sont stockés dans le dossier `logs/` et sont rotés automatiquement (10MB par fichier, 5 fichiers de backup).
