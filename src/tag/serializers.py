from rest_framework import serializers

from tag.models import Tag
from posts.api.serializers import PostSerializer

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
        ]


class TagWithPostsSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)
    
    class Meta:
        model = Tag
        fields = [
            "name",
            "posts"
        ]