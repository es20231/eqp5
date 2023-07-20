from api import views
from django.urls import path

app_name = "api"

urlpatterns = [
    path("sign-up/", views.UsersAPIView.as_view(), name="sign-up-users"),
]
