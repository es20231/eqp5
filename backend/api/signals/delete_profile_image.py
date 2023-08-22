from api.models import Profile
from api.utils import delete_image
from django.db.models.signals import pre_delete
from django.dispatch import receiver


@receiver(pre_delete, sender=Profile)
def delete_profile_image(sender, instance, *args, **kwargs):
    if old_instance := Profile.objects.filter(id=instance.id).first():
        delete_image(old_instance)
