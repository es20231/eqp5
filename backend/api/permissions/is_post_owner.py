from rest_framework.permissions import BasePermission


class IsPostOwner(BasePermission):
    message = "Você só pode alterar os seus próprios posts"
    def has_object_permission(self, request, view, obj):  
        return request.user.id == obj.profile.user.id