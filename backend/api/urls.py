from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from api.serializers import CustomJWTSerializer
from api import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "api"

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(serializer_class=CustomJWTSerializer), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('logout/', views.LogoutAPIView.as_view(), name="api_logout"),
    path('users/', views.UserAPIView.as_view(), name="user_api_list"),
    path('users/<int:id>/', views.UserAPIView.as_view(), name="user_api_detail"),
    path('profiles/', views.ProfileAPIView.as_view(), name="profile_api_list"),
    path('profiles/<int:id>/', views.ProfileAPIView.as_view(), name="profile_api_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
