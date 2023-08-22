from rest_framework import serializers
from api.models import Connection


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ["id", "user", "following"]
        read_only_fields = ["user"]