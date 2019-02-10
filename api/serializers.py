from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

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

#
# User
#


User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data
