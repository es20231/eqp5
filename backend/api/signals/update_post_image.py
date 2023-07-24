from api.models import Post
from api.utils import delete_image
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=Post)
def update_post_image(sender, instance, *args, **kwargs):
    old_instance = Post.objects.filter(id=instance.id).first()
    if not old_instance:
        return
    is_new_image = old_instance.image != instance.image
    if is_new_image:
        delete_image(old_instance)
