from api.models import RemarkReaction
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


@receiver(pre_delete, sender=RemarkReaction)
def remove_like_or_dislike_remark(sender, instance: RemarkReaction, using, origin, **kwargs: dict) -> None:
    remark = instance.remark
    if instance.reaction == "like":
        remark.number_of_likes -= 1
    if instance.reaction == "dislike":
        remark.number_of_dislikes -= 1
    remark.save()