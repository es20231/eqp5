from api.models import Remark
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Remark)
def create_post_remark(sender, instance: Remark, created: bool, **kwargs: dict) -> None:
    post = instance.post
    if created:
        post.number_of_remarks += 1
    post.save()