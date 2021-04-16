from django.conf import settings
from django.db import models

from posts.utils import get_post_upload_image_path


User = settings.AUTH_USER_MODEL


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=get_post_upload_image_path, blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return f"{self.title}"


#Creating new model
class Product(models.Model):
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to=get_post_upload_image_path, blank=True, null=True)
    name = models.TextField(max_length=65)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    
