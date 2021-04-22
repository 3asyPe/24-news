from rest_framework.decorators import api_view
from rest_framework.response import Response

from categories.models import Category
from categories.serializers import CategorySerializer


@api_view(["GET"])
def get_category_api(request):
    data = request.GET  #id
    print(request.__dict__)
    id = data.get("id")

    if id is None:
        return Response({"error": f"category id is required"})

    category = Category.objects.get(
        id=id
    )

    serializer = CategorySerializer(instance=category)

    print(request.GET)

    return Response(serializer.data, status=200)   