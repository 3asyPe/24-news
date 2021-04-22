from django.urls import path

from posts.api import apis


urlpatterns = [
    path("api/post/get/", apis.get_post_api),
]
