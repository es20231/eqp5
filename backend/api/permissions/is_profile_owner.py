from rest_framework.permissions import BasePermission


class IsProfileOwner(BasePermission):
    message = "Você só pode alterar as informações do seu próprio perfil."
    def has_object_permission(self, request, view, obj):  
        return request.user.id == obj.user.id