import os
import random
import string


def generate_random_string(size=10, chars=string.ascii_lowercase + string.digits) -> str:
    return "".join(random.choice(chars) for _ in range(size))


def get_upload_image_path(instance, filename: str, prefix: str,) -> str:
    new_filename = generate_random_string()
    name, ext = get_filename_ext(filename)
    final_filename = f"{new_filename}{ext}"
    return f"{prefix}/{final_filename}"


def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(filename)
    return name, ext
