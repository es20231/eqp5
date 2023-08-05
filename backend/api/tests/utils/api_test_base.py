from django.urls import reverse
from api.models import User
from typing import List

class APITestBase:
    def _init_(self) ->  None:
        self.views_urls = {
            "user": {
                "get": {
                    "list": "/api/users/",
                    "detail": "/api/users/"
                },
                "post": {
                    "list": "/api/users/"
                },
                "patch": {
                    "detail": "/api/users/"
                }
            },
            "post": {},
            "profile": {}
        }
    def create_user(
        self,
        full_name="Jhon Doe",
        username="jhondoe",
        email="jhondoe@email.com",
        password="qaz12345",
    ) -> User:
        return User.objects.create_user(
            full_name=full_name,
            username=username,
            email=email,
            password=password
        )
    
    def create_user_set(self, quant: int = 10) -> List[User]:
        users_set = []
        for i in range(quant + 1):
            user_info = {
                    "username": f"user{i + 1}",
                    "full_name": f"Full Name User{i + 1}",
                    "email": f"user{i + 1}@gmail.com",
                    "password": "qaz12345",
                }
            user = self.create_user(**user_info)
            users_set.append(user)
        return users_set
    
    def get_user_data(self):
        return {
            "username": "jhondoe",
            "email": "jhondoe@email.com",
            "password": "qaz12345",
            "full_name": "Jhon Doe",
        }
    
    def get_tokens(self):
        user = self.create_user(**self.get_user_data())
        response = self.client.post(
            path=reverse("api:token_obtain_pair"),
            data={
                "email": "jhondoe@email.com",
                "password": "qaz12345"
            }
        )
        return {
            "access": response.data.get("access"),
            "refresh": response.data.get("refresh"),
            "user": user
        }
    
    def get_api_url(method: str = "get", view_name: str = "user", action: str = "list") -> str:
        if view_name == "user":
            ...