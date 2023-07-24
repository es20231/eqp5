from api.models import Profile, User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance: User, created: bool, **kwargs: dict) -> None:
    if created:
        Profile.objects.create(user=instance)