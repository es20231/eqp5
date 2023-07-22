from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ProfileSerializer
from api.models import Profile
from api.utils import paginate_response


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
