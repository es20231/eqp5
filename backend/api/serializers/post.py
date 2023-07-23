from api.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    profile = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name="api:profile_api_detail",
        lookup_url_kwarg="id"
    )
    class Meta:
        model = Post
        fields = ["id","image","description", "created_at", "updated_at", "is_posted"]
        read_only_fields = ["created_at", "updated_at"]