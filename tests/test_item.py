from src.item import Item


def test_item():
    """Тестирование класса Item из src/item.py, служащего для представления товара в магазине"""
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

    # устанавливаем новый уровень цен
    item1.pay_rate = 0.8
    # применяем скидку
    item1.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 20000

    assert Item.all == 2
