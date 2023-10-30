from pytest import raises

from src.phone import Phone
from src.item import Item


def test_class_phone():
    # смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2

    item1 = Item("Смартфон", 1000, 20)

    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

    # Проверка невозможности сложения не экземпляров классов Phone или Item
    with raises(ValueError):
        phone1 + 10


def test_class_phone__number_of_sim():
    phone1 = Phone("iPhone 14", 120000, 5, 2)

    assert phone1.number_of_sim == 2

    # Число сим-карт не может быть равным нулю
    with raises(ValueError):
        phone1.number_of_sim = 0

    # Число сим-карт не может быть равным отрицательному числу
    with raises(ValueError):
        phone1.number_of_sim = -1

    # Число сим-карт не может быть равным вещественному числу
    with raises(ValueError):
        phone1.number_of_sim = 1.0

    # Число сим-карт не может быть равным строковому значению
    with raises(ValueError):
        phone1.number_of_sim = "1"
