from api.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","image","description", "created_at", "updated_at", "is_posted"]
        read_only_fields = ["created_at", "updated_at"]