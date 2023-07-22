from django.db import models
from api.models import Profile


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=False, upload_to="posts/images/%Y/%m/%d")
    description = models.CharField(max_length=1000, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("-id",)
        db_table = "posts"