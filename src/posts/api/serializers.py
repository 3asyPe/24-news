from rest_framework import serializers

from posts.models import Post
from posts.models import Product


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "update",
            "timestamp",
        ]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "description",
            "image",
            "name",
            "price",
            "id"
        ]