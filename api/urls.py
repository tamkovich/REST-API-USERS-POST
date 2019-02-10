from django.urls import path, re_path

from api.views import (
    # post
    PostListAPIView,
    PostCreateAPIView,
    PostDetailAPIView,
    PostMarkAPIView,
    # user
    UserCreateAPIView,
    UserLoginAPIView,
)

from rest_framework_simplejwt import views as jwt_views

app_name = 'api'

urlpatterns = [
    # post
    path('post/list/', PostListAPIView.as_view(), name='post-list'),
    path('post/create/', PostCreateAPIView.as_view(), name='post-create'),
    re_path('post/(?P<id>[0-9]+)/$', PostDetailAPIView.as_view(), name='post-detail'),
    re_path('post/(?P<id>[0-9]+)/(?P<mark>[\w-]+)/$', PostMarkAPIView.as_view(), name='post-mark'),

    # user
    path('user/login/', UserLoginAPIView.as_view(), name='user-login'),
    path('user/register/', UserCreateAPIView.as_view(), name='user-register'),
    path('user/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
