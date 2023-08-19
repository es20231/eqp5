from api.models import PostReaction
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=PostReaction)
def like_or_dislike_post(sender, instance: PostReaction, created: bool, **kwargs: dict) -> None:
    post = instance.post
    if created and instance.reaction == "like":
        post.number_of_likes += 1
    if created and instance.reaction == "dislike":
        post.number_of_dislikes += 1
    post.save()