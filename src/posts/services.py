from decimal import Decimal

from posts.models import Product


# Services for business logic

def get_create_product(
    description: str,
    name: str,
    price: Decimal
) -> Product:
    return Product.objects.get_or_create(
        description=description,
        name=name,
        price=price,
    )
