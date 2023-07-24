from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    message = "Você só pode alterar as informações de usuário da sua própria conta"
    def has_object_permission(self, request, view, obj):  
        return request.user.id == obj.id