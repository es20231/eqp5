from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "Você só pode alterar as informações da sua própria conta"
    def has_object_permission(self, request, view, obj):  
        return request.user.id == obj.id