from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer
from api.models import User


class UserAPIView(APIView):
    permission_classes = [IsAuthenticated,]
