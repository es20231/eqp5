from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from api.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=300, blank=True, null=False)
    username = models.CharField(max_length=150, blank=False, null=False, unique=True)
    email = models.CharField(max_length=150, blank=False, null=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "full_name"]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ("-id",)
        db_table = "users"
