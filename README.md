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
Le dépôt Git contient les éléments suivantes.

- [] src/ contient les codes sources Python principaux du projet, en particulier les codes du producer (déjà présent) et du consumer.
- [] data/ contient les données du projet.
- [] config/ contient les configurations et paramètres du projet.
- [] LICENSE.txt : licence du projet.
- [] requirements.txt : liste des dépendances Python nécessaires.
- [] README.md : fichier d'accueil.
- [] Premiers pas
Les instructions suivantes permettent d'exécuter le projet sur son PC.

### Pré-requis
Le projet nécessite Python 3 d'installé sur le système.

>[!NOTE]Installation
> Cloner le projet Git.

> git clone [https://github.com/Franck-F/Projet-Data-Science-Apache-Kafka-Fraud-Detection.git]
> Installer les dépendances du fichier requirements.txt dans un environnement virtuel.

> Linux / MacOS
```
python3 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
```
Windows
```
python3 -m venv venv/
C:\<chemin_dossir>\venv\Scripts\activate.bat
pip install -r requirements.txt
```
