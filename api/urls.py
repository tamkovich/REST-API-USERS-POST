from django.urls import path

from api.views import (
    PostListAPIView,
    PostCreateAPIView
)

app_name = 'api'

urlpatterns = [
    path('post/list/', PostListAPIView.as_view(), name='post-list'),
    path('post/create/', PostCreateAPIView.as_view(), name='post-create'),
]
