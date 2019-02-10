from django.urls import path, re_path

from api.views import (
    # post
    PostListAPIView,
    PostCreateAPIView,
    PostDetailAPIView,
    PostMarkAPIView,
    PostRandomMarkAPIView,
    # user
    UserCreateAPIView,
    UserLoginAPIView,
)

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

app_name = 'api'

urlpatterns = [
    # post
    path('post/list/', PostListAPIView.as_view(), name='post-list'),
    path('post/create/', PostCreateAPIView.as_view(), name='post-create'),
    re_path('post/random/(?P<mark>[\w-]+)/$', PostRandomMarkAPIView.as_view(), name='post-random-mark'),
    re_path('post/(?P<id>[0-9]+)/$', PostDetailAPIView.as_view(), name='post-detail'),
    re_path('post/(?P<id>[0-9]+)/(?P<mark>[\w-]+)/$', PostMarkAPIView.as_view(), name='post-mark'),

    # user
    path('user/login/', UserLoginAPIView.as_view(), name='user-login'),
    path('user/register/', UserCreateAPIView.as_view(), name='user-register'),
    path('user/token/', obtain_jwt_token, name='token_obtain_pair'),
    path('user/token-verify/', verify_jwt_token),
]


'''
curl -X POST -d "username=AutoBot0&password=autobotpasswordcommon" http://127.0.0.1:8000/api/user/token/

<token>

curl -H "Authorization: JWT <token>" http://127.0.0.1:8000/api/post/list/

curl -X POST -H "Authorization: JWT <token>" -H "Content-Type: application/json" -d '{"content":"some post test", "title": "OpaTest"}' 'http://127.0.0.1:8000/api/post/create/'

curl http://127.0.0.1:8000/api/post/list/

curl -X POST -d "username=admin&password=123123abc" http://127.0.0.1:8000/api/user/token/

<token>

curl -X POST -H "Authorization: JWT <token>" -H "Content-Type: application/json" -d '{"content":"new post test", "title": "WowTest"}' 'http://127.0.0.1:8000/api/post/create/'

'''
