from posts.models import Post


def get_5_random_posts():
    posts = Post.objects.order_by('?')[:4] #получаем 5 рандомных постов
    return posts