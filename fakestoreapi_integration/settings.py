"""
Django settings for fakestoreapi_integration project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--xr5jl5!srkd(4lk3-oc7imp_pxc_+g1qw+bxt=xlk1mtu7u1a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'fakestoreapi_integration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_q'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fakestoreapi_integration.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Q_CLUSTER = {
#     'name': 'fakestoreapi_integration',
#     'workers': 2,
#     'recycle': 500,
#     'timeout': 60,
#     'compress': True,
#     'save_limit': 250,
#     'queue_limit': 500,
#     'cpu_affinity': 1,
#     'label': 'Django Q',
#     'redis': {
#         'host': '127.0.0.1',
#         'port': 6379,
#         'db': 0, }
# }

Q_CLUSTER = {
    'name': 'fakestoreapi_integration',
    'orm': 'default',
    'timeout': 60
}

WSGI_APPLICATION = 'fakestoreapi_integration.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

import os

POSTGRES_DB = {
        "port": os.environ.get("DB_PORT", "5432"),
        "host": os.environ.get("DB_HOST", "localhost"),
        "user": os.environ.get("DB_USER", "django"),
        "password": os.environ.get("DB_PASSWORD", "django"),
        "name": os.environ.get("DB_NAME", "django")
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': POSTGRES_DB["name"],
        'USER': POSTGRES_DB["user"],
        'PASSWORD': POSTGRES_DB["password"],
        'HOST': POSTGRES_DB["host"],
        'PORT': POSTGRES_DB["port"],
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
