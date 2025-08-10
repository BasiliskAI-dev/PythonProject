import pytest
from main import Product, Category


@pytest.fixture
def product_cucumber() -> Product:
    return Product('Огурец', 'Зеленый овощ', 120.5, 5)

def test_init(product_cucumber):
    assert product_cucumber.name == 'Огурец'
    assert product_cucumber.description == 'Зеленый овощ'
    assert product_cucumber.price == 120.5
    assert product_cucumber.quantity == 5

def test_category_initialization():
    product1 = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 5)
    product2 = Product("Телефон", "Смартфон с хорошей камерой", 699.99, 10)

    electronics = Category("Электроника", "Техника для дома", [product1, product2])

    assert electronics.name == "Электроника"
    assert len(electronics.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2