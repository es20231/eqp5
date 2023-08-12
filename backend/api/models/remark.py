from django.db import models
from api.models import User, Post


class Remark(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=500, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="remarks")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="remarks")
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Remark {self.id} by {self.user.username} on post {self.post.id}"

    @property
    def username(self):
        return self.user.username

    @property
    def post_id(self):
        return self.post.id

    class Meta:
        verbose_name = "Remark"
        verbose_name_plural = "Remarks"
        ordering = ("-id",)
        db_table = "remarks"