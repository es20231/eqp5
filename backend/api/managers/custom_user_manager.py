from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def __field_error(self, field, message):
        if not field:
            raise ValueError(message)

    def create_user(self, username, email, password, **other_fields):
        self.__field_error(username, "A user must have a username")
        self.__field_error(email, "A user must have a email address")
        self.__field_error(password, "A user should have a password")

        user = self.model(
            username=username, email=self.normalize_email(email), **other_fields
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, phone_number, password, **other_fields):
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("validated_user", True)

        user = self.create_user(username, email, phone_number, password, **other_fields)
        user.save()
        return user
