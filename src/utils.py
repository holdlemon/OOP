import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """ Открываем файл для чтения и возвращаем данные """
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: dict) -> list:
    """ Считывает данные и создает объекты классов """
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories


if __name__ == "__main__":
    path_str = read_json("../data/products.json")
    result = create_objects_from_json(path_str)
    print(result[0].name)
    print(result[0].description)
    print(result[0].products)
