from django.urls import path\

from . import views


# РАЗБЕРИ
urlpatterns = [
    path('hello/', views.hello),
]
