from django.urls import path, re_path

from api.views import (
    PostListAPIView,
    PostCreateAPIView,
    PostDetailAPIView,
    PostMarkAPIView,
)

app_name = 'api'

urlpatterns = [
    path('post/list/', PostListAPIView.as_view(), name='post-list'),
    path('post/create/', PostCreateAPIView.as_view(), name='post-create'),
    re_path('post/(?P<id>[0-9]+)/$', PostDetailAPIView.as_view(), name='post-detail'),
    re_path('post/(?P<id>[0-9]+)/(?P<mark>[\w-]+)/$', PostMarkAPIView.as_view(), name='post-mark'),
]
