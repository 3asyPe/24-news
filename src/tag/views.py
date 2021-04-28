from rest_framework.response import Response
from rest_framework.decorators import api_view

from tag.models import Tag
from tag.serializers import TagSerializer


@api_view(["GET"])
def get_tag_api(request):
    data = request.GET
    id = data.get("id")

    if id is None:
        return Response({"error": f"Tag id is required"})

    tag = Tag.objects.get(
        id=id
    )

    serializer = TagSerializer(instance=tag)
    return Response(serializer.data, status=200)
