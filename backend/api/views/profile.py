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

    def get_queryset(self):
        return Profile.objects.all()
    
    def get_object(self) -> Profile:
        id = self.kwargs.get("id")
        profile = self.get_queryset().get(id=id)
        self.check_object_permissions(self.request, profile)
        return profile
    
    def get(self, request: HttpRequest, id: int = None) -> Response:
        try:
            if id:
                object = self.get_queryset().get(id=id)
                results = ProfileSerializer(instance=object, context={"request": request}).data
            if not id:
                params = request.query_params.copy()
                params = {key: params[key] for key in params.keys()}
                per_page = int(params.pop("per_page", 10))
                page = int(params.pop("page", 1))
                objects = self.get_queryset()
                results = paginate_response(
                    items=objects,
                    serializer=ProfileSerializer,
                    per_page=per_page,
                    page=page,
                    context= {"request": request}
                )
            return Response(data=results, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request: HttpRequest, id: int) -> Response:
        try:
            profile = self.get_object()
            serializer = ProfileSerializer(data=request.data, instance=profile, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)