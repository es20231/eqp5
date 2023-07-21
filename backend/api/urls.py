from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from api import views

app_name = "api"

urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/', views.UserAPIView.as_view(), name="user_api_list"),
    path('users/<int:id>/', views.UserAPIView.as_view(), name="user_api_detail"),   
]
