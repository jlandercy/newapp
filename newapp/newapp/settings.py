"""
Django settings for newapp project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import binascii
import pathlib

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
APP_PACKAGE = pathlib.Path(__file__).parent.parent
APP_NAME = os.environ.get('APP_NAME', APP_PACKAGE.parts[-1])
BASE_DIR = str(APP_PACKAGE)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('APP_SECRETKEY', binascii.hexlify(os.urandom(64)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('APP_DEBUG', True))

ALLOWED_HOSTS = [os.environ.get('APP_HOST', 'localhost')]


# Application definition

INSTALLED_APPS = [
    'polls.apps.PollsConfig',  # Dummy app from tutorial
    # -----
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # -----
    'crispy_forms',
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

ROOT_URLCONF = APP_NAME + '.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = APP_NAME + '.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('APP_DATABASE_NAME', APP_NAME),
        'USER': os.environ.get('APP_DATABASE_USER', 'django'),
        'PASSWORD': os.environ.get('APP_DATABASE_PASSWORD', 'django'),
        'HOST': os.environ.get('APP_DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('APP_DATABASE_PORT', '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'

# https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'