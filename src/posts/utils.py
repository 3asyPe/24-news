from app.utils import get_upload_image_path


def get_post_upload_image_path(*args, **kwargs):
    return get_upload_image_path(*args, **kwargs, prefix="posts")
