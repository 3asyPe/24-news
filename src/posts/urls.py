from django.urls import path

from . import views


urlpatterns = [
    path("api/post/get/", views.get_post_api),
]
