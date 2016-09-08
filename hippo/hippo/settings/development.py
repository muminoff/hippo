import os
from hippo.settings import *  # noqa

DEBUG = True
INSTALLED_APPS.append('debug_toolbar')  # noqa
BACKEND_ENDPOINT_URL = 'http://192.168.99.100:8080'
BACKEND_ACCESS_KEY = os.getenv('ACCESS_KEY')
BACKEND_SECRET_KEY = os.getenv('SECRET_KEY')
