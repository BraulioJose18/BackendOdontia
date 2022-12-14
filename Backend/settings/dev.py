from django.template.backends import django

from Backend.settings import *

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DEBUG = True
ALLOWED_HOSTS = [
    '*'
]
THIRD_APPS = [
    'rest_framework',
    'corsheaders',
    'django_filters',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'drf_yasg',
]
OWN_APPS = [
    'apps.products',
    'apps.user',
    'apps.kardex'
]
INSTALLED_APPS = FIRST_APPS + THIRD_APPS + OWN_APPS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'odontia',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '',
        'PORT': '5432',
    }
}
# Database Config
