from django.conf import settings
from django.db import models

from posts.utils import get_post_upload_image_path


User = settings.AUTH_USER_MODEL


class Post(models.Model):
    slug = models.SlugField(blank=True, default="") # имя отформатированное под url 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to=get_post_upload_image_path, blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('tag.Tag', related_name='posts', blank=True) #(related_name, где posts - название поля) , blank - пустое поле лакально, null - пустое поле в db

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return f"{self.title}"
