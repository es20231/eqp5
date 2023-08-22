from api.models import User
from api.serializers import UserSerializer
from api.utils import paginate_response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q


class SerachAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def get_params(self) -> dict:
        params = self.request.query_params.copy()
        return {key: params[key] for key in params.keys()}

    def post(self, request: HttpRequest) -> Response:
        try:
            params = self.get_params()
            page = int(params.pop("page", 1))
            per_page = int(params.pop("per_page", 10))
            data = request.data
            if "search" in data:
                search = data.pop("search")
            else:
                raise Exception("It is necessary to send the search field")
            results = User.objects.filter(Q(username__icontains=search) | Q(full_name__icontains=search)).order_by("-id")
            results = paginate_response(
                items=results,
                per_page=per_page,
                page=page,
                serializer=UserSerializer,
                context={"request": request}
            )
            return Response(data=results, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)