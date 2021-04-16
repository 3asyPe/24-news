from django.urls import path

from . import views


urlpatterns = [
    path("api/post/get/", views.get_post_api),
    path("api/product/get/", views.get_product_api),
    path("api/product/create/", views.create_product_api),
    
]
