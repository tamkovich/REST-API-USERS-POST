from django.urls import path

from api.views import (
    PostListAPIView
)

app_name = 'api'

urlpatterns = [
    path('post/list/', PostListAPIView.as_view(), name='post-list'),
]
