from rest_framework.decorators import api_view
from rest_framework.response import Response

from posts.models import Post
from posts.models import Product
from posts.serializers import PostSerializer


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

#HOMEWORK HERE
#GET, POST, DELETE, PUT
@api_view(["Get"])
def get_product_api(request, *args, **kwargs):
    product_id = request.GET.get("id")
    if product_id in None:
        return Response({"error": f"Product with id - {product_id} does not exist"}, status=400)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": f"Product with id - {product_id} does not exist"}, status=400)

    serializer = ProductSerializer(instance=Product)
    return Response(serializer.data, status = 200)


@api_view(["PUT"])
def put_product_api(request, *args, **kwargs):
    product_id = request.PUT.put("id")
    if product_id in None:
        return Response({"error": f"Product with id - {product_id} does not exist"}, status=400)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": f"Product with id - {product_id} does not exist"}, status=400)

    serializer = ProductSerializer(instance=Product)
    return Response(serializer.data, status = 200)


@api_view(["DELETE"])
def del_product_api(request, *args, **kwargs):
    product_id = request.DELETE.delete("id")
    if product_id in None:
        return Response({"error": f"Product with id - {product_id} does not exist"}, status=400)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": f"Product with id - {product_id} does not exist"}, status=400)

    serializer = ProductSerializer(instance=Product)
    return Response(serializer.data, status = 200)


@api_view(["POST"])
def post_product_api(request, *args, **kwargs):
    product_id = request.POST.post("id")
    if product_id in None:
        return Response({"error": f"Product with id - {product_id} does not exist"}, status=400)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": f"Product with id - {product_id} does not exist"}, status=400)

    serializer = ProductSerializer(instance=Product)
    return Response(serializer.data, status = 200)
