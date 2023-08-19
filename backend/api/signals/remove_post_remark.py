from api.models import Remark
from django.db.models.signals import pre_delete
from django.dispatch import receiver


@receiver(pre_delete, sender=Remark)
def remove_post_remark(sender, instance: Remark, using, origin, **kwargs: dict) -> None:
    post = instance.post
    post.number_of_remarks -= 1
    post.save()