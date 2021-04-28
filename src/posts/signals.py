from django.db.models.signals import pre_save
from django.dispatch import receiver

from app.utils import generate_unique_slug
from posts.models import Post


# sender - модель, что мы тригерим
# instance - объект, что вызвал тригер. Например данный объект сохранили
# created - если объект первый раз сохранен (создан) - True, иначе - False
@receiver(pre_save, sender=Post)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = generate_unique_slug(instance=instance)
        instance.slug = slug
