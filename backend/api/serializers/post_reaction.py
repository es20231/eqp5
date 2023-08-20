from rest_framework import serializers
from api.models import PostReaction


class PostReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReaction
        fields = ["id", "created_at", "user", "username", "post", "reaction"]
        read_only_fields = ["created_at", "user", "username"]