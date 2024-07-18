import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def first_category():
    return Category(
        name="Телефоны",
        description="Телефоны улучшают качество жизни",
        products=[
            Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15 Pro Max", "256GB, Серый цвет, 1000MP камера", 175000.0, 2)
        ]
    )


@pytest.fixture
def second_category():
    return Category(
        name="Телевизоры",
        description="Улучшают просмотр Ютуба в домашних условиях",
        products=[
            Product("Lenovo Ultra 4K", "Full HD, 4к формат", 200000.0, 3),
            Product("LG", "Ultra Full HD, 8к формат", 300000.0, 1),
            Product("Xiaomi", "Full HD, есть LED-подсветка", 180000.0, 6)
        ]
    )


@pytest.fixture
def product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
