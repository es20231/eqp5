from api.models import RemarkReaction
from api.serializers import RemarkReactionSerializer
from api.utils import paginate_response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from api.permissions import IsRemarkReactionOwner


class RemarkReactionAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def get_params(self) -> dict:
        params = self.request.query_params.copy()
        return {key: params[key] for key in params.keys()}

    def get_sort_direction(self, params: dict) -> str:
        sort_direction = int(params.pop("sort_direction", -1))
        if sort_direction not in [1, -1]:
            raise ValueError("The sort_direction filter should be 1 or -1.")
        return "-" if sort_direction == -1 else ""

    def get_order_by(self, params: dict) -> str:
        allowed_ordering_fields = ["created_at", "updated_at"]
        order_by = params.pop("order_by", "updated_at")
        if order_by not in allowed_ordering_fields:
             raise ValueError(f"The value of the order_by field must be one of the following: {allowed_ordering_fields}")
        return order_by

    def get_permissions(self):
        if self.request.method in ["DELETE", "PATCH"]:
            return [IsRemarkReactionOwner(),]
        return super().get_permissions()
    
    def get_object(self) -> RemarkReaction:
        id = self.kwargs.get("id")
        remark_like = RemarkReaction.objects.get(id=id)
        self.check_object_permissions(request=self.request, obj=remark_like)
        return remark_like

    def get(self, request: HttpRequest, id: int = None) -> Response:
        try:
            if not id:
                params = self.get_params()
                filters = {}
                page = int(params.pop("page", 1))
                per_page = int(params.pop("per_page", 10))
                ordering = f"{self.get_sort_direction(params)}{self.get_order_by(params)}"
                if "remark_id" in params:
                    filters["remark"] = int(params.pop("remark_id"))
                if "reaction" in params:
                    filters["reaction"] = params.pop("reaction")
                else:
                    raise Exception("It is necessary to send remark_id and reaction filters")
                results = RemarkReaction.objects.filter(**filters).order_by(ordering)
                results = paginate_response(
                    items=results,
                    per_page=per_page,
                    page=page,
                    serializer=RemarkReactionSerializer,
                    context={"request": request}
                )
            if id:
                results = RemarkReaction.objects.get(id=id)
                results = RemarkReactionSerializer(instance=results, context={"request": request}).data
            return Response(data=results, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request: HttpRequest) -> Response:
        try:
            data = request.data
            reaction = "dislike" if data.get("reaction") == "like" else "like"
            remark_reaction = RemarkReaction.objects.all().filter(user__id=request.user.id, reaction=reaction)
            if remark_reaction:
                remark_reaction.first().delete()
            serializer = RemarkReactionSerializer(data=data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: HttpRequest, id: int) -> Response:
        try:
            remark_like = self.get_object()
            remark_like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
