from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from api.serializers import CustomJWTSerializer
from api import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "api"

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(serializer_class=CustomJWTSerializer), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/', views.UserAPIView.as_view(), name="user_api_list"),
    path('users/<int:id>/', views.UserAPIView.as_view(), name="user_api_detail"),
    path('users/forgot-password/', views.ForgotPasswordAPIView.as_view(), name="forgot_password"),
    path('profiles/', views.ProfileAPIView.as_view(), name="profile_api_list"),
    path('profiles/<int:id>/', views.ProfileAPIView.as_view(), name="profile_api_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
