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
fraud_detection_system/
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

### Utilisation
1. Collecte des données :
```bash
python src/data/data_collector.py
```

2. Entraînement du modèle :
```bash
python src/models/train.py
```

3. Démarrer le système en temps réel :
```bash
python src/kafka/consumer.py
```

## Tests
```bash
pytest tests/
```
