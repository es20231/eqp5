from api.models import User
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView
import string as s
from django.core.mail import send_mail
from random import SystemRandom as SR
from django.conf import settings


class ForgotPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    def __raise_email_error(self, email: str):
        if not email:
            raise Exception("Campo 'email' vazio, ensira um e-mail de usuário cadastrado")
        
    def get_user_by_email(self) -> User:
        self.__raise_email_error(self.request.data.get("email"))
        return User.objects.get(email=self.request.data.get("email"))

    def crete_recovery_password(self) -> str:
        punctuation = '@#$%&*!?'
        return ''.join(SR().choices(s.ascii_letters + punctuation + s.digits, k=12))
    
    def change_user_password(self, user: User) -> str:
        recovery_password = self.crete_recovery_password()
        user.set_password(recovery_password)
        user.save()
        return recovery_password
    
    def get_email_format(self, user: User, recovery_password) -> dict:
        return {
            "subject": "PostBook - Senha Temporária",
            "message": f"Oi, {user.full_name}!\n\nVocê solicitou a recuperação de senha, abaixo está a senha criada para que você acesse a sua conta e crie uma nova senha.\n\nSenha de recuperação: {recovery_password}\n\nAté breve!\n\nEquipe de Suporte/PostBook",
            "recipient_list": [user.email],
            "from_email": settings.EMAIL_HOST_USER
        }
    
    def send_recovery_password_email(self) -> None:
        user = self.get_user_by_email()
        recovery_password = self.change_user_password(user)
        email_format = self.get_email_format(user, recovery_password)
        return send_mail(**email_format)

    def post(self, request: HttpRequest) -> User:
        try:
            assert self.send_recovery_password_email() == 1, "Erro ao criar senha de recuperação"
            return Response(status=status.HTTP_201_CREATED)
        except Exception as error:
            message = str(error)
            code = status.HTTP_400_BAD_REQUEST
            if message == "User matching query does not exist.":
                message = "Não existe usuário cadastrado com esse endereço de e-mail"
                code = status.HTTP_404_NOT_FOUND
            return Response(data={"error": message}, status=code)
