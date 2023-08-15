from api.models import PostReaction
from api.serializers import PostReactionSerializer
from api.utils import paginate_response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from api.permissions import IsReactionOwner


class PostReactionAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def get_params(self) -> dict:
        params = self.request.query_params.copy()
        return {key: params[key] for key in params.keys()}

    def get_permissions(self):
        if self.request.method in ["DELETE"]:
            return [IsReactionOwner(),]
        return super().get_permissions()
    
    def get_object(self) -> PostReaction:
        id = self.kwargs.get("id")
        post_reaction = PostReaction.objects.get(id=id)
        self.check_object_permissions(request=self.request, obj=post_reaction)
        return post_reaction

    def get(self, request: HttpRequest, id: int = None) -> Response:
        try:
            if not id:
                params = self.get_params()
                filters = {}
                page = int(params.pop("page", 1))
                per_page = int(params.pop("per_page", 10))
                if "post_id" in params:
                    filters["post"] = int(params.pop("post_id"))
                if "reaction" in params:
                    filters["reaction"] = params.pop("reaction")
                else:
                    raise Exception("It is necessary to send post_id and reaction filters")
                results = PostReaction.objects.filter(**filters).order_by("-created_at")
                results = paginate_response(
                    items=results,
                    per_page=per_page,
                    page=page,
                    serializer=PostReactionSerializer,
                    context={"request": request}
                )
            if id:
                results = PostReaction.objects.get(id=id)
                results = PostReactionSerializer(instance=results, context={"request": request}).data
            return Response(data=results, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request: HttpRequest) -> Response:
        try:
            data = request.data
            post_reaction = PostReaction.objects.all().filter(user=request.user.id, post=data["post"])
            if post_reaction:
                post_reaction.first().delete()
            serializer = PostReactionSerializer(data=data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: HttpRequest, id: int) -> Response:
        try:
            post_reaction = self.get_object()
            post_reaction.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
