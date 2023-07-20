import os
from datetime import timedelta

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost",
]


REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.MultiPartParser",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "SIGNING_KEY": os.environ.get("JWT_SECRET_KEY"),
    "AUTH_HEADER_TYPES": ("Bearer",),
}
