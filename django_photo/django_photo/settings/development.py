# load defaults and override with devlopment settings
from defaults import *

DEBUG = True

WSGI_APPLICATION = 'django_photo.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django-photo',
        'USER': 'Administrator',
        'PASSWORD': 'administrator'
    }
}
