from api.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        many=False,
        view_name="api:user_api_detail",
        read_only=True,
        lookup_url_kwarg="id"
    )
    class Meta:
        model = Profile
        fields = ["id", "description", "user", "image"]
