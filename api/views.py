from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Post
from api.serializers import (
    PostListSerializer,
    PostCreateSerializer,
    PostDetailSerializer,
)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'


class PostMarkAPIView(APIView):

    @staticmethod
    def _get_object(id):
        try:
            return Post.objects.get(pk=id)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, id, mark, format=None):
        post = self._get_object(id)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)

    def put(self, request, id, mark, format=None):
        post = self._get_object(id)
        if mark == 'like':
            post.likes += 1
            post.save()
        elif mark == 'dislike':
            post.dislike += 1
            post.save()
        else:
            raise Http404
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)
