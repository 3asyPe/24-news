from rest_framework.response import Response
from rest_framework.decorators import api_view

from tag.models import Tag
from tag.serializers import TagSerializer, TagWithPostsSerializer
from tag.services import get_top_tags



@api_view(["GET"])
def get_tag_api(request):
    data = request.GET
    id = data.get("id")

    if id is None:
        return Response({"error": f"Tag id is required"})

    tag = Tag.objects.get(
        id=id
    )

    serializer = TagWithPostsSerializer(instance=tag)
    return Response(serializer.data, status=200)


@api_view(["GET"])
def get_top_tags_api(request):
    tags = get_top_tags()
    serializer = TagSerializer(instance=tags, many=True)
    return Response(serializer.data, status=200)


