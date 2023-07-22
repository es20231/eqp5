from rest_framework import serializers
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "full_name", "username", "email", "validated_user", "is_active", "is_superuser"]

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
    
    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop("password")
        instance.set_password(password)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance