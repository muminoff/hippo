import os
from hippo.settings import *  # noqa

DEBUG = True
BACKEND_ENDPOINT_URL = os.getenv('BACKEND_ENDPOINT_URL', 'http://192.168.99.100:8080')  # noqa
BACKEND_ACCESS_KEY = os.getenv('ACCESS_KEY')
BACKEND_SECRET_KEY = os.getenv('SECRET_KEY')
