from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


# РАЗБЕРИ
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("posts.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
