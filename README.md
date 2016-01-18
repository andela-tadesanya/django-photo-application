# django-photo-application
A Django powered photo editing app
[![Coverage Status](https://coveralls.io/repos/andela-tadesanya/django-photo-application/badge.svg?branch=master&service=github)](https://coveralls.io/github/andela-tadesanya/django-photo-application?branch=master)  [![Build Status](https://travis-ci.org/andela-tadesanya/django-photo-application.svg?branch=master)](https://travis-ci.org/andela-tadesanya/django-photo-application)

## Introduction
A Django based photo editing app that uses Pillow to manipulate and create effects on images.

## Features
- Facebook Sign-up and Sign-in
- Country flag effects
- Sharing on Facebook

## Testing
From the root directory run `python django_photo/manage.py test photo`

## Installation
- Download/Clone the repo
- cd into the project root in your favorite commandline tool
- Run `pip install -r requirements.txt` to install all dependencies
- Create an environment variable `DJANGO_ENVIRONMENT` with the value 'development', 'production', or 'testing' depending on the environment
- Run `python django_photo/manage.py makemigrations` and then run `python django_photo/manage.py migrate` to create tables in the database
- Run `python django_photo/manage.py runserver` to start the server

## Version
1.0.0

## Demo
http://shutterpix.herokuapp.com/

## Credit
God, Google, Me
