import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
DEBUG = os.environ.get("DEBUG") == "1"
ALLOWED_HOSTS = []
ROOT_URLCONF = "core.urls"
WSGI_APPLICATION = "core.wsgi.application"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "api.User"
AUTHENTICATION_BACKENDS = ["api.backends.email_backend.EmailBackend"]
