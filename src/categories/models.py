from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    posts = models.ForeignKey('posts.Post', on_delete=models.SET_NULL, blank=True, null=True) # OneToMany
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return f"{self.name}"

    
