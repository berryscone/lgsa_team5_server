import logging
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-@xa3q7=z6^4hjn@uu#v3#r4*z_c*2%837#gg3qdrd7+e)x_w_i'
DEBUG = False
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'rest_framework',
    'knox',
    'vehicle_query_app',
    'health_check',
    'health_check.db',
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

ROOT_URLCONF = 'vehicle_query_service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'vehicle_query_service.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'deuk4qkmuc9r07',
        'USER': 'seqyxpdbxcadyn',
        'PASSWORD': '95cc0658a115f3807fba283108c0d2b156b5ab3436c824263b6d329c2e0df2f4',
        'HOST': 'ec2-3-222-74-92.compute-1.amazonaws.com',
        'PORT': 5432
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = False

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'vehicle_query_service.custom_handlers.custom_exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'knox.auth.TokenAuthentication',
    ],
}

REST_KNOX = {
    'TOKEN_TTL': None  # without expiry time
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    "formatters": {
        "default": {
            "format": "%(asctime)s %(levelname).1s %(filename)s:%(lineno)3d - %(message)s"
        },
    },
    'filters': {
        'info_filter': {
            '()': 'vehicle_query_service.custom_filters.LevelFilter',
            'level': logging.INFO,
        }
    },
    'handlers': {
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'default',
            'filename': 'logs/django_debug.log',
            'when': "midnight",
            'backupCount': 5,
        },
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'default',
            'filters': ['info_filter'],
            'filename': 'logs/django_info.log',
            'when': "midnight",
            'backupCount': 5,
        }
    },
    'root': {
        'handlers': ['debug', 'info'],
        'level': 'DEBUG',
    },
}
