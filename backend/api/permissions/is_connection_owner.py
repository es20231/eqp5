from rest_framework.permissions import BasePermission


class IsConnectionOwner(BasePermission):
    message = "Logged in user can only undo their connections"
    
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.user.id