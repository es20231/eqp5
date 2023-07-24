from rest_framework import serializers
from api.models import User
from django.core.mail import send_mail
from django.conf import settings


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

    def get_email_format(self, user: User) -> dict:
        return {
            "subject": "PostBook - Conta Criada com Sucesso",
            "message": f"Oi, {user.full_name}!\n\nSua conta no PostBook está pronta.Se você não se cadastrou no PostBook recentemente, por favor ignore este email.\n\nAté breve!\n\nEquipe de Suporte/PostBook",
            "recipient_list": [user.email],
            "from_email": settings.EMAIL_HOST_USER
        }

    def send_created_account_email(self, user: User) -> int:
        try:
            email_format = self.get_email_format(user)
            return send_mail(**email_format)
        except Exception as error:
            return 0

    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(**validated_data)
        email = self.send_created_account_email(user)
        return user
    
    def update(self, instance: User, validated_data: dict) -> User:
        if password := validated_data.pop("password", None):
            instance.set_password(password)
        for key, value in validated_data.items():
            if key in ["username"]: continue
            setattr(instance, key, value)
        instance.save()
        return instance