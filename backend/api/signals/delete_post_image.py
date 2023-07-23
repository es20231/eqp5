from api.models import Post
from api.utils import delete_image
from django.db.models.signals import pre_delete
from django.dispatch import receiver


@receiver(pre_delete, sender=Post)
def delete_profile_photo(sender, instance, *args, **kwargs):
    if old_instance := Post.objects.filter(id=instance.id).first():
        delete_image(old_instance)
