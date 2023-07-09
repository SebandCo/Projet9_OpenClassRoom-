[![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg?style=plastic)](https://badge.fury.io/py/tensorflow)

# Projet9_OpenClassRoom-
Projet 9  dans le cadre de la formation OpenClassRoom developpeur d'application Python

# Descriptif
Interface web permettant la mise en ligne de Ticket et leurs Critiques
Le projet est construit avec du CSS (Sass) et du HTML
Il utilise une interface Django
Le projet est un MVP, il est donc d'aspect un peu brut

# Installation
## Pré-requis
Créer un environnement dédié
```
$ python -m venv env
```
A l'intérieur de l'environnement installer les packages
```
$ pip install -r requirements.txt
```
## La base de donnée
La base de donnée est existante dans le dépot au format sqlite3

Vous pouvez néanmoins un créer un nouvelle en :
1. Supprimant le fichier db.sqlite3
1. Créant un nouvelle base de donnée
```
python manage.py migrate
```

## Lancement du programme
Le programme se lance grâce à la commande
```
python manage.py runserver
```
Puis en allant sur un navigateur web :
[LITReview] (http://127.0.0.1:8000/)

# Contribution
Commençant en programmation Python, et notamment Django, je suis preneur :
1. des détections de bug
2. des suggestions d'amélioration du code
3. des suggestions d'amélioration de la documentation
