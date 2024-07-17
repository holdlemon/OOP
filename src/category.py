from src.product import Product


class Category:
    name: str
    description: str
    products: list
    count_category = 0
    count_products = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.count_category += 1
        Category.count_products += len(products) if products else 0


if __name__ == "__main__":
    prod1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    prod2 = Product("Iphone 15 Pro Max", "256GB, Серый цвет, 1000MP камера", 175000.0, 2)
    prod3 = Product("Xiaomi", "16GB, Белый цвет, 5MP камера", 12000.0, 9)
    prod4 = Product("Nokia", "8GB, Черный цвет, 3MP камера", 6000.0, 15)

    category = Category("Телефоны", "Мобильные телефоны, для улучшения качества жизни", [prod1, prod2, prod3, prod4])
    print(category.name)
    print(category.description)
    print(category.products)
    print(category.count_category)
    print(category.count_products)
