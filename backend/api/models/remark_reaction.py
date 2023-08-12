from django.db import models
from api.models import Remark, User


class RemarkReaction(models.Model):
    REACTION_TYPES = (
        ("like", "Like"),
        ("dislike", "Dislike")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="remark_reactions")
    remark = models.ForeignKey(Remark, on_delete=models.CASCADE, related_name="remark_reactions")
    reaction = models.CharField(max_length=8, choices=REACTION_TYPES, null=False, blank=False)
    
    @property
    def user_id(self):
        return self.user.pk
    
    @property
    def username(self):
        return self.user.username

    class Meta:
        verbose_name = "RemarkReaction"
        verbose_name_plural = "RemarkReactions"
        ordering = ("-updated_at",)
        db_table = "remark_reactions"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "remark"],
                name="remark_cant_be_liked_or_desliked_twice_by_same_user"
            ),
        ]