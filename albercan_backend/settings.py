import logging
from pathlib import Path

from envsqare import Environment

env = Environment()

ENVS_FOLDER = Path("envs")
ENVIRONMENT_READ_VARNAME = "ENV_LOADED"

env_path = str((ENVS_FOLDER / f"{env('ALBERCAN_ENV') or ''}.env").absolute())
try:
    env.read_env(env_path)
except FileNotFoundError:
    logging.warning(f"Environment file {env_path} not found.")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_NAME = "albercan_backend"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.BOOL('DEBUG', False)

ALLOWED_HOSTS = env.LIST('ALLOWED_HOSTS', [])

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "people",
    "pet",
    "structure"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "albercan_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / PROJECT_NAME / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "albercan_backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "es-bo"

LOCALE_PATHS = [
    BASE_DIR / "locale",
]

TIME_ZONE = "America/La_Paz"
USE_I18N = True
USE_TZ = True

TIME_FORMAT = "H:i"
DATETIME_FORMAT = "d/m/Y H:i:s"
DATE_FORMAT = "d/m/Y"

TIME_INPUT_FORMATS = ["%H:%M"]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = env("STATIC_URL", "static/")
STATIC_ROOT = env('STATIC_ROOT')  # This is when I run the app in prod
STATIC_ROOT = f'{(BASE_DIR / STATIC_ROOT).absolute()}' if STATIC_ROOT else None
STATICFILES_DIRS = [
    BASE_DIR / PROJECT_NAME / "static"
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
