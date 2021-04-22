from rest_framework.decorators import api_view
from rest_framework.response import Response

from posts.api.serializers import PostSerializer
from posts.models import Post


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




        
    






