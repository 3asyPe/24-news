from django.db.models import Count
from tag.models import Tag


def get_top_tags():
    return Tag.objects.annotate(count_of_posts=Count('posts')) \
            .order_by('count_of_posts')[:9] #annotate привязывает, order_by return
                