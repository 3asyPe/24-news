from django.urls import path

from posts.api import apis


urlpatterns = [
    path("api/post/get/", apis.get_post_api),
    path("api/product/get/", apis.get_product_api),
    path("api/product/create/", apis.create_product_api),
    path("api/product/delete/", apis.delete_product_api),
    path("api/product/change/", apis.put_product_api),  
]
