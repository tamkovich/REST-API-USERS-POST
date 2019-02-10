from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from api.models import Post


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'creator',
        ]


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'created_at',
            'creator',
            'likes',
            'dislikes',
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'created_at',
            'creator',
            'likes',
            'dislikes',
        ]
