from rest_framework.permissions import BasePermission


class IsRemarkFromUserPost(BasePermission):
    message = "Logged in user can only delete comments on own post"
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.post.profile.user.id