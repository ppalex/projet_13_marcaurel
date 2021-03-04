from . import *
import os

FIXTURE_DIRS = (os.path.join('tests', 'fixtures'),)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TEST': {
            'NAME': 'mytestdatabase',
        }
    },
}
