# Projet 13:

## Description

The goal of this project is to help amateur football players to organize their football games.

This project aims to facilitate the search for football games and players thanks to a localization system.


## Features

* Create game
* Invite players
* Localize games or players
* Find players or game near your location
* Alert players around a game


## Language

* Python

## Framework

* Django (https://www.djangoproject.com/)

## Library

* GeoDjango (https://docs.djangoproject.com/en/3.1/ref/contrib/gis/)
* Celery (https://docs.celeryproject.org/en/stable/)
* Leaflet (https://leafletjs.com/)

## Database

* Postgresql
* Redis



## Installation using Docker


* Prerequisite

You need to add a ".env.dev" file that contains the dev environnement data:

```
DEBUG=1
SECRET_KEY=dev
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] 
INTERNAL_IPS=['127.0.0.1']
SQL_ENGINE=django.contrib.gis.db.backends.postgis
SQL_DATABASE=gis
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db
SQL_PORT=5432
MAPQUEST_API_KEY=
CELERY_BROKER=redis://redis:6379/0
CELERY_BACKEND=redis://redis:6379/0
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_PORT=587
EMAIL_USE_TLS=True
```

* To install the application with Docker and Docker Compose, launch the command:

```
docker-compose build
```


## Launch the app

```
docker-compose up
```