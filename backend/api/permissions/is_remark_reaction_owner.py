from rest_framework.permissions import BasePermission


class IsRemarkReactionOwner(BasePermission):
    message = "The logged in user can only add or remove the likes or dislikes he has made"

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.user.id