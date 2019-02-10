from rest_framework.generics import ListAPIView, CreateAPIView

from api.models import Post
from api.serializers import PostListSerializer, PostCreateSerializer


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
