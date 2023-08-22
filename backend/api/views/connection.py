from api.models import Connection
from api.serializers import ConnectionSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from api.permissions import IsConnectionOwner


class ConnectionAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def get_params(self) -> dict:
        params = self.request.query_params.copy()
        return {key: params[key] for key in params.keys()}

    def get_permissions(self):
        if self.request.method in ["DELETE"]:
            return [IsConnectionOwner(),]
        return super().get_permissions()
    
    def get_object(self) -> Connection:
        id = self.kwargs.get("id")
        connection = Connection.objects.get(id=id)
        self.check_object_permissions(request=self.request, obj=connection)
        return connection
    
    def post(self, request: HttpRequest) -> Response:
        try:
            data = request.data
            serializer = ConnectionSerializer(data=data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: HttpRequest, id: int = None) -> Response:
        try:
            if id:
                connection = self.get_object()
                connection.delete()
            if params := self.get_params():
                connection = Connection.objects.get(user=request.user, following__username=params.pop("username"))
                connection.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)