from api.models import Post, Profile
from api.serializers import PostSerializer
from api.utils import paginate_response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from api.permissions import IsPostOwner


class PostAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def get_user_profile(self) -> Profile:
        user_id = self.request.user.id
        return Profile.objects.all().get(user__id=user_id)

    def get_queryset(self):
        return Post.objects.all()

    def get_object(self, **kwargs) -> Post:
        id = self.kwargs.get("id")
        post = self.get_queryset().get(id=id, **kwargs)
        self.check_object_permissions(self.request, post)
        return post
    
    def get_permissions(self):
        if self.request.method in ["PATCH", "DELETE"]:
            return [IsAuthenticated(), IsPostOwner()]
        return super().get_permissions()
    
    def format_query_strings(self) -> dict:
        params = self.request.query_params.copy()
        return {key: params[key] for key in params.keys()}

    def post(self, request: HttpRequest) -> Post:
        try:
            serializer = PostSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save(profile=self.get_user_profile())
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request: HttpRequest, id:int = None) -> Response:
        try:
            if id:
                filters = {
                    "is_posted": eval(request.query_params.pop("is_posted", "True").title())
                }
                object = self.get_object(**filters)
                results = PostSerializer(instance=object, context={"request": request}).data
            elif not id:
                params = request.query_params.copy()
                params = {key: params[key] for key in params.keys()}

                per_page = int(params.pop("per_page", 10))
                page = int(params.pop("page", 1))
                order_by = params.pop("order_by", "created_at")
                sort_direction = "-" if int(params.pop("sort_direction", -1)) == -1 else ""
                ordering = f"{sort_direction}{order_by}"

                filters = {}

                if "is_posted" in params:
                    filters["is_posted"] = eval(params.pop("is_posted").title())
                if "created_at" in params:
                    filters
                if "profile_id" in params:
                    filters["profile__id"] = params.pop("profile_id")
                if "user_id" in params:
                    filters["profile__user__id"] = params.pop("user_id")
                if "username" in params:
                    filters["profile__user__username"] = params.pop("username")
                if "my_posts" in params:
                    filters["profile__user__id"] = self.request.user.id
                
                objects = self.get_queryset().filter(**filters)

                results = paginate_response(
                    items=objects,
                    serializer=PostSerializer,
                    per_page=per_page,
                    page=page,
                    context= {"request": request}
                )

            return Response(data=results, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request: HttpRequest, id: int = None) -> Response:
        try:
            filters = {
                "is_posted": eval(request.query_params.pop("is_posted", "True").title())
            }
            post = self.get_object(**filters)
            serializer = PostSerializer(instance=post, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request: HttpRequest, id: int = None) -> Response:
        try:
            filters = {
                "is_posted": eval(request.query_params.pop("is_posted", "True").title())
            }
            post = self.get_object(**filters).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(data={"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)