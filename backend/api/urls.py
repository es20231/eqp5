from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from api.serializers import CustomJWTSerializer
from api import views


app_name = "api"

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(serializer_class=CustomJWTSerializer), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('logout/', views.LogoutAPIView.as_view(), name="api_logout"),
    path('users/me/', views.MeAPIView.as_view(), name="user_me_api"),
    path('users/', views.UserAPIView.as_view(), name="user_api_list"),
    path('users/<int:id>/', views.UserAPIView.as_view(), name="user_api_detail"),
    path('users/forgot-password/', views.ForgotPasswordAPIView.as_view(), name="api_forgot_password"),
    path('profiles/', views.ProfileAPIView.as_view(), name="profile_api_list"),
    path('profiles/<int:id>/', views.ProfileAPIView.as_view(), name="profile_api_detail"),
    path('posts/', views.PostAPIView.as_view(), name="post_api_list"),
    path('posts/<int:id>/', views.PostAPIView.as_view(), name="post_api_detail"),
    path('remarks/', views.RemarkAPIView.as_view(), name="remark_api_list"),
    path('remarks/<int:id>/', views.RemarkAPIView.as_view(), name="remark_api_detail"),
    path('remark-reactions/', views.RemarkReactionAPIView.as_view(), name="remark_reaction_api_list"),
    path('remark-reactions/<int:id>/', views.RemarkReactionAPIView.as_view(), name="remark_reaction_api_detail"),
    path('post-reactions/', views.PostReactionAPIView.as_view(), name="post_reaction_api_list"),
    path('search/', views.SerachAPIView.as_view(), name="search_api_list"),
]