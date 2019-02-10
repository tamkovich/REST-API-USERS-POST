from rest_framework.serializers import ModelSerializer

from api.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'created_at',
            'creator',
        ]
