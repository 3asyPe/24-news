from rest_framework.decorators import api_view
from rest_framework.response import Response

from posts.api.serializers import PostSerializer, ProductSerializer
from posts.api.validators import CreateProductSerializer
from posts.models import Post, Product
from posts.services import get_create_product


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
#GET, POST, DELETE, PUT - обновить (product.variable = variable)

@api_view(["GET"])
def get_product_api(request, *args, **kwargs):
    product_id = request.GET.get("id")
    if product_id is None:
        return Response({"error": "Product id is required"}, status=400)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": f"Product with id - {product_id} does not exist"}, status=400)
    
    serializer = ProductSerializer(instance=product)
    return Response(serializer.data, status=200)


@api_view(["POST"])
def create_product_api(request):
    data = request.POST or request.data
    validator = CreateProductSerializer(data=data)
    validator.is_valid(raise_exception=True)

    product = Product.objects.create(
        description=data["description"],
        name=data["name"],
        price=data["price"],
    )
    serializer = ProductSerializer(instance=product)
    return Response(serializer.data, status=201)


@api_view(["POST"])
def delete_product_api(request):
    data = request.POST or request.data #got id product
    product_id = data.get('id') #saved in variable
    if product_id is None:
        return Response({"error": "Product id is required"}, status=400)
    try:
        product = Product.objects.get(id=product_id) #made request in data
    except Product.DoesNotExist:
        return Response({"error": f"product with id {product_id} does not exist"}, status=400)

    product.delete()
    return Response({"message": "deleted successfully"}, status=200)  # {} - empty json object
    






