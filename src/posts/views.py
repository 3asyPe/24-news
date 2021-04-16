from rest_framework.decorators import api_view
from rest_framework.response import Response

from posts.models import Post, Product
from posts.serializers import PostSerializer, ProductSerializer


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
    description = data.get('description')
    name = data.get('name')
    price = data.get('price')
    print(request.POST)
    print(data)
    if description is None:
         return Response({"error": "Product description is required"}, status=400)
    if name is None:
        return Response({"error": "Product name is required"}, status=400)
    if price is None:
        return Response({"error": "Product price is required"}, status=400)

    product = Product.objects.create(
        description=description,
        name=name,
        price=price
    )
    serializer = ProductSerializer(instance=product)
    return Response(serializer.data, status=201)






    


