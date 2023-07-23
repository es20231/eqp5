from rest_framework import serializers
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.HyperlinkedRelatedField(
        many=False,
        view_name="api:profile_api_detail",
        read_only=True,
        lookup_url_kwarg="id"
    )
    class Meta:
        model = User
        fields = ["id", "full_name", "username", "email", "password", "is_active", "is_superuser", "profile"]

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
    
    def update(self, instance: User, validated_data: dict) -> User:
        if password := validated_data.pop("password", None):
            instance.set_password(password)
        for key, value in validated_data.items():
            if key in ["username"]: continue
            setattr(instance, key, value)
        instance.save()
        return instance