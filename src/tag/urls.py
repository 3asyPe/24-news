from django.urls import path

from tag import views


urlpatterns = [
    path("api/tag/get/", views.get_tag_api)
]