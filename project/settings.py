import os
import environ
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')
DEBUG = bool(int(env('DEBUG')))
# DEBUG = False

#ALLOWED_HOSTS = ['82.148.28.107', '127.0.0.1', 'localhost']
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.sites',
    # 'django.contrib.redirects',

    'app',
    'livereload',
    'webp_converter',
    'django_webp',
    'rest_framework',
]

MIDDLEWARE_CLASSES = (
    # 'livesync.core.middleware.DjangoLiveSyncMiddleware'
    'livereload.middleware.LiveReloadScript',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.contrib.redirects.middleware.RedirectFallbackMiddleware'

    'livereload.middleware.LiveReloadScript'
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.abspath(BASE_DIR), '#assets'),
            os.path.join(os.path.abspath(BASE_DIR), 'app', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # 'webp_converter.context_processors.webp_support',
                # 'django_webp.context_processors.webp',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [
            os.path.join(os.path.abspath(BASE_DIR), '#assets'),
            os.path.join(os.path.abspath(BASE_DIR), 'app', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'auto_reload': True,
            'trim_blocks': True,
            'lstrip_blocks': True,
            'environment': 'project.jinja2_settings.environment',
            'context_processors': [
                # 'webp_converter.context_processors.webp_support',
                # 'django_webp.context_processors.webp',
            ]
        },
    }
]

WSGI_APPLICATION = 'project.wsgi.application'

dev_bases = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
prod_bases = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbms_db',
        'USER': 'www',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DATABASES = dev_bases if DEBUG else prod_bases

# DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}


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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/staticfiles/'
MEDIA_URL = '/mediafiles/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
]


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True

# CSRF_COOKIE_SECURE = True
# CSRF_USE_SESSIONS = True

CSRF_TRUSTED_ORIGINS = [
    '82.148.28.107',
    'bumeranger.ru',
    'www.bumeranger.ru',
    '127.0.0.1:8080',
    'localhost:8080',
]

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:8080',
    'http://localhost:8080',
]

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8080',
    'http://localhost:8080',
]

CORS_ALLOW_ALL_ORIGINS = True
