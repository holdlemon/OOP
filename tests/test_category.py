def test_category_init(first_category, second_category):
    assert first_category.name == "Телефоны"
    assert first_category.description == "Телефоны улучшают качество жизни"
    assert len(first_category.products) == 2
    assert second_category.name == "Телевизоры"
    assert second_category.description == "Улучшают просмотр Ютуба в домашних условиях"
    assert len(second_category.products) == 3

    assert first_category.count_category == 2
    assert second_category.count_category == 2

    assert first_category.count_products == 5
    assert second_category.count_products == 5
