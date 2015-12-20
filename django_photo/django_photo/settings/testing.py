# load defaults and override with devlopment settings
from defaults import *

DEBUG = True

WSGI_APPLICATION = 'django_photo.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test.db'),
    }
}
