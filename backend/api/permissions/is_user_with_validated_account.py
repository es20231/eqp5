from rest_framework.permissions import BasePermission


class IsUserWithValidatedAccount(BasePermission):
    message = f"Conta cadastrada, mas não validada"

    def has_permission(self, request, view):
        self.user = request.user
        return bool(self.user.validated_user)
