from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

from posts.api.serializers import PostSerializer
from posts.models import Post
from posts.services import get_5_random_posts


class PostsListPagination(generics.ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Post.objects.order_by('-timestamp')




@api_view(["GET"])
def get_post_api(request, *args, **kwargs):
    post_id = request.GET.get("id")
    if post_id is None:
        return Response({"error": "Post id is required"}, status=400)

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"error": f"Post with id - {post_id} does not exist"}, status=400)

    serializer = PostSerializer(instance=post)
    return Response(serializer.data, status=200)


@api_view(["GET"])
def get_main_posts_api(request, *args, **kwargs):
    posts = get_5_random_posts()
    
    serializer = PostSerializer(instance=posts, many=True)
    return Response(serializer.data, status=200)


