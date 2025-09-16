from pathlib import Path
from decouple import config

# Rutas base
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY y DEBUG vía variables de entorno
SECRET_KEY = config('SECRET_KEY', default='django-insecure-rbz-bj-ux1w9wpz7%#d-9r)ni-6709j&7is)+0hq*kyw=c0ls5')
DEBUG = config('DEBUG', default=False, cast=bool)

# Dominios permitidos
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost').split(',')

# Aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ElTotem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ElTotem.wsgi.application'

# Base de datos MySQL (local)
DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE', default='django.db.backends.mysql'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='3306'),
        'NAME': config('DB_NAME', default='eltotem_db'),
        'USER': config('DB_USER', default='eltotem_user'),
        'PASSWORD': config('DB_PASSWORD', default='ClaveTotem_2025!'),
    }
}

# Internacionalización
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Otros ajustes
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
