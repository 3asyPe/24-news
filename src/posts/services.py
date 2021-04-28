from posts.models import Post


def get_5_random_posts():
    posts = Post.objects.order_by("?")[:5] #получаем 5 рандомных постов
    return posts

