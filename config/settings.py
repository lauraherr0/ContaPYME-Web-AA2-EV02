import os
from pathlib import Path
from secrets import token_urlsafe

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY") or token_urlsafe(48)
DEBUG = False
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "testserver"]
ROOT_URLCONF = "config.urls"
INSTALLED_APPS = ["usuarios"]
MIDDLEWARE = ["django.middleware.common.CommonMiddleware", "django.middleware.csrf.CsrfViewMiddleware"]
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "APP_DIRS": True,
}]
DATABASES = {"default": {
    "ENGINE": "django.db.backends.mysql",
    "NAME": "software_contable_pymes",
    "HOST": "127.0.0.1",
    "PORT": os.getenv("MYSQL_PORT", "3307"),
    "USER": os.getenv("MYSQL_USER", "root"),
    "PASSWORD": os.getenv("MYSQL_PASSWORD", ""),
    "OPTIONS": {"charset": "utf8mb4"},
}}
LANGUAGE_CODE = "es-co"
TIME_ZONE = "America/Bogota"
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
