"""
Django settings for groupmebot project on Heroku. Fore more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import dj_database_url
from . import localcreds
import psycopg2

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

#DEPLOYMENT MODE : toggle LOCAL or REMOTE
DEPLOY = os.environ.get('P3GRPMEBOT_DEPLOYMENT_MODE')

#Secret keys for heroku (deploy must be LOCAL or REMOTE)
def SECRET_KEYS(deploy):
    if (deploy == 'LOCAL'):
        return (localcreds.get_credentials(django=True), 
                localcreds.get_credentials(firebase=True),
                localcreds.get_credentials(groupme=True),
                localcreds.get_credentials(postgres=True))
    elif (deploy == 'REMOTE'):
        return (os.environ.get('GROUPMEBOT_DJANGO_SECRET_KEY'), 
                os.environ.get('GROUPMEBOT_FIREBASE_SECRET_KEY'),
                os.environ.get('GROUPMEBOT_GROUPME_SECRET_KEY'),
                os.environ.get('GROUPMEBOT_POSTGRES_SECRET_KEY')
                ) 
    else:
        print ('BAD DEPLOMENT CONDITION!')
        assert(False)

(SECRET_KEY, GROUPMEBOT_FIREBASE_SECRET_KEY, GROUPMEBOT_GROUPME_SECRET_KEY, GROUPMEBOT_POSTGRES_SECRET_KEY) = SECRET_KEYS(DEPLOY)

# SECURITY WARNING: don't run with debug turned on in production!
if (DEPLOY == 'LOCAL'):
    DEBUG = True
else:
    DEBUG = False

FIREBASE_URL = "https://groupmebot-4104f.firebaseio.com/"
CALLBACK_URL = "https://ilyasgroupmebot.herokuapp.com/behave"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'bot'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'groupmebot.urls'

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
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'groupmebot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

if (DEPLOY == "REMOTE"):
    # Update database configuration with $DATABASE_URL.
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)
elif (DEPLOY == "LOCAL"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'local_p3grpmebot',
            'USER': 'ilya',
            'PASSWORD': GROUPMEBOT_POSTGRES_SECRET_KEY,
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else:
    print("BAD DEPLOYMENT CONDITION!")
    assert(False)
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
