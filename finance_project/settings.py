import os
from pathlib import Path
import dj_database_url

# ========================
# Paths
# ========================
BASE_DIR = Path(__file__).resolve().parent.parent

# ========================
# Security
# ========================
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "fallback-secret-key")
DEBUG = os.environ.get("DJANGO_DEBUG", "False") == "True"
ALLOWED_HOSTS = os.environ.get(
    "DJANGO_ALLOWED_HOSTS", "financetracker-xgd0.onrender.com"
).split(",")


# ========================
# Installed Apps
# ========================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    # external apps
    "django_extensions",
    "widget_tweaks",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "django_filters",
    "django_htmx",
    "template_partials",
    "import_export",
    # project apps
    "tracker",
]

# Убираем debug_toolbar из продакшн
if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")

SITE_ID = 1

# ========================
# Middleware
# ========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
]

if DEBUG:
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

ROOT_URLCONF = "finance_project.urls"

# ========================
# Templates
# ========================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "finance_project" / "templates"],
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

WSGI_APPLICATION = "finance_project.wsgi.application"

# ========================
# Database
# ========================
DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}

# ========================
# Password validation
# ========================
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

# ========================
# Internationalization
# ========================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ========================
# Static files
# ========================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# ========================
# Default primary key
# ========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ========================
# Internal / debug
# ========================
INTERNAL_IPS = ["127.0.0.1"]

# ========================
# Auth & login
# ========================
AUTH_USER_MODEL = "tracker.User"
LOGIN_REDIRECT_URL = "index"
PAGE_SIZE = 5

# ========================
# Email (для allauth)
# ========================
EMAIL_BACKEND = (
    "django.core.mail.backends.console.EmailBackend"  # временно, можно менять на SMTP
)
