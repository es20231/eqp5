from rest_framework import serializers
from api.models import Remark


class RemarkSerializer(serializers.ModelSerializer):
    user_url = serializers.HyperlinkedRelatedField(
        many=False,
        view_name="api:user_api_detail",
        read_only=True,
        lookup_url_kwarg="id",
        source="user"
    )
    class Meta:
        model = Remark
        fields = ["id", "created_at", "updated_at", "text", "user_url", "user", "username", "post", "likes", "dislikes"]
        read_only_fields = ["likes", "user"]

    def create(self, validated_data: dict) -> Remark:
        return Remark.objects.create(**validated_data)