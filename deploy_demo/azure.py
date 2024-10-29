import os
from settings import *

SECRET_KEY = os.environ.get("SECRET_KEY") #'django-insecure-hitk&np3jj+70-751npuj*w17xb#8wtyhr#lkkw_-5)w##3$(2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG") == 'True'

ALLOWED_HOSTS =  os.environ.get("AZURE_ALLOWED_HOSTS").split(" ")


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Enables whitenoise for serving static files
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
