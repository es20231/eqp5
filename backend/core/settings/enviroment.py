from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = "insecure_keyIdLHSP7jghKVrPxU6dfo6lg0esXvsYDC"
DEBUG = True
ALLOWED_HOSTS = []
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
