from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Tag")
        verbose_name_plural = ("Tags")

    def __str__(self):
        return f"{self.name}"