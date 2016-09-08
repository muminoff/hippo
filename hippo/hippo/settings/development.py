import os
from hippo.settings import *  # noqa

DEBUG = True
INSTALLED_APPS.append('debug_toolbar')  # noqa
BACKEND_ACCESS_KEY = os.getenv('ACCESS_KEY')
BACKEND_SECRET_KEY = os.getenv('SECRET_KEY')
