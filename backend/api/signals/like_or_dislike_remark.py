from api.models import RemarkReaction
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=RemarkReaction)
def like_or_dislike_remark(sender, instance: RemarkReaction, created: bool, **kwargs: dict) -> None:
    remark = instance.remark
    if created and instance.reaction == "like":
        remark.number_of_likes += 1
    if created and instance.reaction == "dislike":
        remark.number_of_dislikes += 1
    remark.save()