from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer
)
from django.contrib.auth import get_user_model

from api.models import Post


class PostCreateSerializer(ModelSerializer):
    creator = CharField(read_only=True)

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
            'creator',
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
        user_obj = User.objects.create_user(
            username,
            email,
            password
        )
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()
    email = EmailField(allow_blank=True, label='Email Address')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',

        ]
        extra_kwargs = {
            "password":
                {"write_only": True}
        }

