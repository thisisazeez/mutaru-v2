"""
Django settings for pmp project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
# from decouple import config
#import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '97=ti2+&!62ss9(*zr%5#h+0a7)@vmueug@zcs!2kp^o2+@6p#'
#SECRET_KEY = config('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = config('DEBUG', default=False, cast=bool)


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django_filters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'mda',
    'lga',
    'project',
    'users',
    'pwa'
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

ROOT_URLCONF = 'pmp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

#WSGI_APPLICATION = 'pmp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

#DATABASES = {'default': dj_database_url.config(default=config('DATABASE_URL'))}


DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'MET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'users/static'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


AUTH_USER_MODEL = 'users.User'
MEDIA_URL = '/media/'
LOGOUT_REDIRECT_URL = 'project:project_list'
LOGIN_REDIRECT_URL = 'project:dashboard'


# pwa
PWA_SERVICE_WORKER_PATH = os.path.join(
    BASE_DIR, 'users/static/js', 'serviceworker.js')


PWA_APP_NAME = 'Mu Gyara'
PWA_APP_DESCRIPTION = "Mu Taru Mu Gyara"
PWA_APP_THEME_COLOR = '#4285F4'
PWA_APP_BACKGROUND_COLOR = '#4285F4'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [
    {
        'src': 'static/img/icon-512x512.png',
        'sizes': '512x512'
    }
]


# email for authentication 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mutarumugyara@gmail.com'
EMAIL_HOST_PASSWORD = 'keyboard@123'

