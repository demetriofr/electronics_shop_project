import pytest

from src.phone import Phone
from src.item import Item


def test_class_phone():
    # смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2

    item1 = Item("Смартфон", 1000, 20)
    phone1.number_of_sim = 0
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

    # Проверка невозможности сложения не экземпляров классов Phone или Item
    with pytest.raises(ValueError):
        phone1 + 10
