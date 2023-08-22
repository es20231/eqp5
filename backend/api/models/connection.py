from django.db import models
from api.models import User
from django.core.exceptions import ValidationError


class Connection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")

    def clean(self) -> None:
        errors = {}
        if self.user.id == self.following.id:
            errors['user'] = "A user can't follow yourself !"
            errors['following'] = "A user can't be followed by yourself!"
        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        if self.user.id == self.following.id:
            raise ValueError("A user can't follow yourself !")
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Connections"
        verbose_name_plural = "Connections"
        ordering = ("-id",)
        db_table = "connections"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "following"],
                name="user_cant_follow_other_twice"
            )
        ]