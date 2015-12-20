"""
WSGI config for django_photo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

# set environment to work in
environment = {
    "development": "django_photo.settings.development",
    "production": "django_photo.settings.production",
    "testing": "django_photo.settings.testing"
}

settings = environment[os.getenv('DJANGO_ENVIRONMENT', 'production')]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
