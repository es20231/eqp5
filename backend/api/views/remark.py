from api.models import Remark
from api.serializers import RemarkSerializer
from api.utils import paginate_response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from api.permissions import IsRemarkFromUserPost, IsRemarkOwner


class RemarkAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def get_permissions(self):
        if self.request.method == "DELETE":
            return [IsAuthenticated(), IsRemarkFromUserPost()]
        if self.request.method == "PATCH":
            return [IsAuthenticated(), IsRemarkOwner()]
        return super().get_permissions()
    
    def get_object(self) -> Remark:
        id = self.kwargs.get("id")
        remark = Remark.objects.get(id=id)
        self.check_object_permissions(request=self.request, obj=remark)
        return remark

    def get_params(self) -> dict:
        params = self.request.query_params.copy()
        return {key: params[key] for key in params.keys()}

    def get_sort_direction(self, params: dict) -> str:
        sort_direction = int(params.pop("sort_direction", -1))
        if sort_direction not in [1, -1]:
            raise ValueError("The sort_direction filter should be 1 or -1.")
        return "-" if sort_direction == -1 else ""

    def get_order_by(self, params: dict) -> str:
        allowed_ordering_fields = ["created_at", "updated_at", "likes"]
        order_by = params.pop("order_by", "updated_at")
        if order_by not in allowed_ordering_fields:
             raise ValueError(f"The value of the order_by field must be one of the following: {allowed_ordering_fields}")
        return order_by

    def get(self, request: HttpRequest, id: int = None) -> Response:
        try:
            if not id:
                params = self.get_params()
                filters = {}
                page = int(params.pop("page", 1))
                per_page = int(params.pop("per_page", 10))
                ordering = f"{self.get_sort_direction(params)}{self.get_order_by(params)}"
                if "post_id" in params:
                    filters["post__id"] = int(params.pop("post_id"))
                else:
                    raise Exception("It is necessary to send the post_id filter")
                results = Remark.objects.filter(**filters).order_by(ordering)
                results = paginate_response(
                    items=results,
                    per_page=per_page,
                    page=page,
                    serializer=RemarkSerializer,
                    context={"request": request}
                )
            if id:
                results = Remark.objects.get(id=id)
                results = RemarkSerializer(instance=results, context={"request": request}).data
            return Response(data=results, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request: HttpRequest) -> Response:
        try:
            data = request.data
            serializer = RemarkSerializer(data=data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: HttpRequest, id: int) -> Response:
        try:
            serializer = RemarkSerializer(
                data=request.data, instance=self.get_object(),
                partial=True, context={"request": request}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: HttpRequest, id: int) -> Response:
        try:
            remark = self.get_object()
            remark.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)