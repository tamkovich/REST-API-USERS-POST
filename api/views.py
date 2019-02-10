from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from rest_framework import status

from django.contrib.auth import get_user_model
from django.http import Http404

from api.models import Post
from api.serializers import (
    # post
    PostListSerializer,
    PostCreateSerializer,
    PostDetailSerializer,
    # user
    UserCreateSerializer,
    UserLoginSerializer,
)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]


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
            post.dislikes += 1
            post.save()
        else:
            raise Http404
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)


class PostRandomMarkAPIView(APIView):

    @staticmethod
    def _get_object(id):
        try:
            return Post.objects.get(pk=id)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, mark, format=None):
        post = Post.objects.random()
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)

    def put(self, request, mark, format=None):
        post = Post.objects.random()
        if mark == 'like':
            post.likes += 1
            post.save()
        elif mark == 'dislike':
            post.dislikes += 1
            post.save()
        else:
            raise Http404
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)

#
# User
#


User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
