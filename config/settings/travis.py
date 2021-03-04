from . import *
import os

FIXTURE_DIRS = (os.path.join('tests', 'fixtures'),)

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'testdatabase',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'db_testing',
        'PORT': '5432',
    },
}
