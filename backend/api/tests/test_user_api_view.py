from api.views import UserAPIView
from rest_framework.test import APITestCase
from django.urls import resolve, reverse
from api.tests.utils import APITestBase
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import base64
import os



class UserAPIViewTest(APITestCase,APITestBase):
    def test_if_post_url_is_correct(self):
        endpoint = reverse("api:user_api_list")
        self.assertEqual("/api/users/", endpoint)

    def test_if_post_returns_status_code_201(self):
        url = reverse("api:user_api_list")
        response = self.client.post(
            path=url,
            data={**self.get_user_data()}
        )
        self.assertEqual(response.status_code, 201)

    def test_if_post_creates_a_user(self):
        url = reverse("api:user_api_list")
        user_data = self.get_user_data()
        response = self.client.post(
            path=url,
            data={**user_data}
        )
        user_created_data = response.data
        self.assertEqual(user_created_data.get("username"), user_data.get("username"))
        self.assertEqual(user_created_data.get("full_name"), user_data.get("full_name"))
        self.assertEqual(user_created_data.get("email"), user_data.get("email"))

    def test_if_unregister_user_can_login(self):
        url = reverse("api:token_obtain_pair")
        response = self.client.post(
            path=url,
            data={
                "email": "user@email.com",
                "password": "P@ssword1234"
            }
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data.get("detail"), "No active account found with the given credentials")
    
    def test_if_registered_user_can_login(self):
        user = self.create_user()
        url = reverse("api:token_obtain_pair")
        response = self.client.post(
            path=url,
            data={
                "email": "jhondoe@email.com",
                "password": "qaz12345"
            }
        )
        self.assertEqual(response.status_code, 200)
    
    def test_forgot_password_error(self):
        url = reverse("api:api_forgot_password")
        response = self.client.post(
            path=url,
            data={
                "email": "jhondoeaa@email.com"
            }
        )
        self.assertEquals(response.status_code,404)
        
    def test_logout_view(self):
        # Obtenha a URL da view de logout usando o nome da URL
        url = reverse("api:api_logout")
        tokens = self.get_tokens()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
        # Envie uma solicitação POST para a URL de logout com o token de refresh
        response = self.client.post(url, {'refresh': tokens['refresh']})

        # Verifique se a resposta tem o status esperado (HTTP 205 RESET CONTENT)
        self.assertEqual(response.status_code, 205)
    def test_profile_get_view(self):
        url = reverse("api:profile_api_list")
        tokens = self.get_tokens()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
        response = self.client.get(url, {'id': 1})

        self.assertEqual(response.status_code, 200)

    def test_upload_post_view(self):
        url = reverse("api:post_api_list")
        tokens = self.get_tokens()

        with open(
            os.path.join(
                os.path.dirname(__file__),
                "test.jpg"
            ),
            'rb'
        ) as fp:
            image_data = fp.read()

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
        response = self.client.post(url, data={'image': SimpleUploadedFile('test.jpg', image_data),
                                          'description':"imagem teste",
                                          'profile':1})

        self.assertEqual(response.status_code, 201)
    
    def test_upload_noAuth_view(self):
        url = reverse("api:post_api_list")
        tokens = self.get_tokens()

        with open(
            os.path.join(
                os.path.dirname(__file__),
                "test.jpg"
            ),
            'rb'
        ) as fp:
            image_data = fp.read()

        response = self.client.post(url, data={'image': SimpleUploadedFile('test.jpg', image_data),
                                          'description':"imagem teste",
                                          'profile':1})

        self.assertEqual(response.status_code, 401)
    
    def test_get_post_view(self):
        url = reverse("api:post_api_list")
        tokens = self.get_tokens()


        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
        response = self.client.get(url, data={'id': 1})

        self.assertEqual(response.status_code, 200)

    def test_recuperacao_email_post_view(self):
        url = reverse("api:api_forgot_password")
        user = self.create_user()

        response = self.client.post(url, data={'email': 'jhondoe@email.com'})

        self.assertEqual(response.status_code, 201)