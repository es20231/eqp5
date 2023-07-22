from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer
from api.models import User


class UserAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return User.objects.all()

    def get_permissions(self, *args, **kwargs):
        if self.request.method == "POST":
            return [AllowAny(),]
        return super().get_permissions(*args, **kwargs)

    def post(self, request: HttpRequest) -> Response:
        try:
            data = request.data
            serializers = UserSerializer(data=data)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: HttpRequest, id: int) -> Response:
        try:
            data = request.data
            instance = User.objects.get(id=id)
            serializers = UserSerializer(data=data, instance=instance, partial=True)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)