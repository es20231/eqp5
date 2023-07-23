from api.models import User
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView
import string as s
from random import SystemRandom as SR

class ForgotPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    def __raise_email_error(self, email: str):
        if not email:
            raise Exception("Campo 'email' vazio, ensira um e-mail de usuário cadastrado")

    def crete_recovery_password(self) -> str:
        punctuation = '@#$%&*!?'
        return ''.join(SR().choices(s.ascii_letters + punctuation + s.digits, k=12))
    
    def change_user_password(self, email: str) -> str:
        user = User.objects.get(email=email)
        recovery_password = self.crete_recovery_password()
        user.set_password(recovery_password)
        user.save()
        return recovery_password

    def post(self, request: HttpRequest) -> User:
        try:
            email = request.data.pop("email", None).lower()
            self.__raise_email_error(email)
            recovery_password = self.change_user_password(email)
            return Response(data={"password": recovery_password}, status=status.HTTP_201_CREATED)
        except Exception as error:
            message = str(error)
            code = status.HTTP_400_BAD_REQUEST
            if message == "User matching query does not exist.":
                message = "Não existe usuário cadastrado com esse endereço de e-mail"
                code = status.HTTP_404_NOT_FOUND
            return Response(data={"error": message}, status=code)
