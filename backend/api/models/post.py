from io import BytesIO
from typing import Iterable, Optional

from api.models import Profile
from django.db import models
from PIL import Image


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=False, upload_to="posts/images/%Y/%m/%d")
    description = models.CharField(max_length=1000, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    is_posted = models.BooleanField(default=False, null=False)

    def save(self, *args, **kwargs) -> None:
        if self.image:
            img = Image.open(self.image)
            img_io = BytesIO()
            img.save(img_io, format=img.format)
            img_size = img_io.tell() 
            size_limit = 10 * 1024 * 1024
            if img_size > size_limit:
                 raise ValueError("A imagem excede o tamanho máximo permitido (10 MB).")
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("-id",)
        db_table = "posts"
