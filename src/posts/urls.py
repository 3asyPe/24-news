from django.urls import path

from posts.api import apis


urlpatterns = [
    path("api/post/get/", apis.get_post_api),
    path("api/post/fetch/main/", apis.get_main_posts_api),
    path("api/post/fetch/last/", apis.PostsListPagination.as_view())
]
