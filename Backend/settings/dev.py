from Backend.settings import *
import pymysql
pymysql.install_as_MySQLdb()

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
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'odontia',
    #     'USER': 'postgres',
    #     'PASSWORD': '123456',
    #     'HOST': '',
    #     'PORT': '5432',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'odontia',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '',
        'PORT': '3306',
    }
}

# Swagger settings
SWAGGER_SETTINGS = {
    'DOC_EXPANSION': 'none',
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    'USE_SESSION_AUTH': True,
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        },
    },
    'JSON_EDITOR': True,
    'SHOW_REQUEST_HEADERS': True,
    'OPERATIONS_SORTER': 'alpha',
    'PERSIST_AUTH': True,
}