from api.models import Post, Profile
from api.serializers import PostSerializer
from api.utils import paginate_response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView


class PostAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def get_user_profile(self) -> Profile:
        user_id = self.request.user.id
        return Profile.objects.all().get(user__id=user_id)

    def post(self, request: HttpRequest) -> Post:
        try:
            serializer = PostSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save(profile=self.get_user_profile())
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)