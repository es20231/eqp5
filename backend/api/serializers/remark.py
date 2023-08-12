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
        fields = ["id", "created_at", "updated_at", "text", "user_url", "user", "username", "post", "number_of_likes", "number_of_dislikes"]
        read_only_fields = ["likes", "user", "number_of_likes", "number_of_dislikes"]

    def create(self, validated_data: dict) -> Remark:
        return Remark.objects.create(**validated_data)