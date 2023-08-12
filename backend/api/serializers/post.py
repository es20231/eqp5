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
        fields = ["id","image","description", "created_at", "profile", "updated_at", "is_posted", "username", "number_of_remarks", "number_of_likes", "number_of_dislikes"]
        read_only_fields = ["created_at", "updated_at", "number_of_remarks", "number_of_likes", "number_of_dislikes"]

    def create(self, validated_data: dict) -> Post:
        if isinstance(validated_data, list):
            return [Post.objects.create(**item) for item in validated_data]
        return Post.objects.create(**validated_data)