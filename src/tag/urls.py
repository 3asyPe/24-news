from django.urls import path
from rest_framework.pagination import PageNumberPagination

from tag import views


urlpatterns = [
    path("api/tag/get/", views.get_tag_api),
    path("api/tag/get/list/", views.get_top_tags_api),
]