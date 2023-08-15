from django.db import models
from api.models import Post, User


class PostReaction(models.Model):
    REACTION_TYPES = (
        ("like", "Like"),
        ("dislike", "Dislike")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_reactions")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_reactions")
    reaction = models.CharField(max_length=10, null=False, choices=REACTION_TYPES)

    @property
    def username(self):
        return self.user.username
    
    class Meta:
        verbose_name = "PostReaction"
        verbose_name_plural = "PostReactions"
        ordering = ("-id",)
        db_table = "post_reactions"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "post"],
                name="user_cant_like_or_dislike_a_post_twice"
            )
        ]