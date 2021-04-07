from django.contrib import admin
from django.urls import path, include

# РАЗБЕРИ
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("posts.urls")),
]
