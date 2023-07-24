from django.db import models
from api.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=500, null=True, blank=True)

    @property
    def username(self) -> str:
        return self.user.username
    
    @property
    def full_name(self) -> str:
        return self.user.full_name

    def __str__(self) -> str:
        return f"Perfil do usuário {self.user.username}"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ("-id",)
        db_table = "profiles"