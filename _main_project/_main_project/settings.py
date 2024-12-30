"""
Django settings for _main_project project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""


import environ, os
from pathlib import Path


env = environ.Env(
	DEBUG=(bool, False)
)

environ.Env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
# DEBUG = False

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# CSRF_TRUSTED_ORIGINS include the hostnames that are allowed to send POST requests without a CSRF token
CSRF_TRUSTED_ORIGINS = ['https://localhost']

# Secure proxy SSL header and secure cookies
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = [
	'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	# adding `sites` app to manage multiple sites and authentication
	'django.contrib.sites',
	'django_htmx',

	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	'allauth.socialaccount.providers.google',

	'_commands',
	'a_chat',
    'a_tournament',
	'a_friends',
	'a_user',
	'a_oauth2',
    'a_game',
    'a_pass',
	'a_spa_frontend'
]

MIDDLEWARE = [
	'django_htmx.middleware.HtmxMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

	'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = '_main_project.urls'

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

# WSGI_APPLICATION = '_main_project.wsgi.application'

ASGI_APPLICATION = '_main_project.asgi.application'

# this will ensure the real-time messages update for all the users in the chatroom
CHANNEL_LAYERS = {
	"default": {
		# 'BACKEND': 'channels.layers.InMemoryChannelLayer'
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            # "hosts": [("127.0.0.1", 6380)],
            "hosts": [("redis-app", 6379)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
	'default': env.db()
}

CACHES = {
	'default': {
		# 'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
		# 'LOCATION': 'game-states-cache',
		'BACKEND': 'django_redis.cache.RedisCache',
		'LOCATION': 'redis://redis-app:6379/1',
		'OPTIONS': {
			'CLIENT_CLASS': 'django_redis.client.DefaultClient',
		},
	}
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


AUTH_USER_MODEL = 'a_user.Account'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static'),
	os.path.join(BASE_DIR, 'media'),
]

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn')

TEMP = os.path.join(BASE_DIR, 'media_cdn/temp')

# BASE_URL = 'http://127.0.0.1:8000'
BASE_URL = 'http://localhost:8000'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# django-allauth settings

AUTHENTICATION_BACKENDS = [
	'django.contrib.auth.backends.AllowAllUsersModelBackend',
	'a_user.backends.CaseInsensitiveModelBackend',
	'django.contrib.auth.backends.ModelBackend',
	'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

DATA_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


# Social account settings
SOCIALACCOUNT_PROVIDERS = {
	'google': {
		'CLIENT_ID': env('GOOGLE_CLIENT_ID'),
		'SECRET': env('GOOGLE_SECRET'),
		'METHOD': 'oauth2',
		'VERIFIED_EMAIL': True,
		'SCOPE': [ 'profile', 'email', ],
		'AUTH_PARAMS': { 'access_type': 'online', },
	},
	'42': {
		'CLIENT_ID': env('42_CLIENT_ID'),
		'SECRET': env('42_SECRET'),
		'METHOD': 'oauth2',
		'VERIFIED_EMAIL': True,
	},
}


if DEBUG:
	EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
