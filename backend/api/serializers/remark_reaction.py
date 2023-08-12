from api.models import RemarkReaction
from rest_framework import serializers


class RemarkReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemarkReaction
        fields = ["id", "created_at", "updated_at", "username", "remark", "reaction"]
        read_only_fields = ["created_at", "updated_at", "username"]
