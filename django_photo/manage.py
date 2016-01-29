#!/usr/bin/env python
import os
import sys

# set environment to work in
environment = {
    "development": "django_photo.settings.development",
    "production": "django_photo.settings.production",
    "testing": "django_photo.settings.testing"
}

settings = environment[os.getenv('DJANGO_ENVIRONMENT', 'development')]

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
