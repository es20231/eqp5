from api.models import PostReaction
from django.db.models.signals import pre_delete
from django.dispatch import receiver


@receiver(pre_delete, sender=PostReaction)
def remove_like_or_dislike_post(sender, instance: PostReaction, using, origin, **kwargs: dict) -> None:
    post = instance.post
    if instance.reaction == "like":
        post.number_of_likes -= 1
    if instance.reaction == "dislike":
        post.number_of_dislikes -= 1
    post.save()