from api.models import Post
from api.serializers import PostSerializer
from api.utils import paginate_response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView


class PostAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    