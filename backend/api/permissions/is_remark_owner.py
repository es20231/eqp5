from rest_framework.permissions import BasePermission


class IsRemarkOwner(BasePermission):
    message = "The logged in user can only edit his own comments"

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.user.id