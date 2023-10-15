from src.item import Item


def test_item():
    """Тестирование класса Item из src/item.py, служащего для представления товара в магазине"""

    # Создаём для экземпляра класса для проведения проверок
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

    # Устанавливаем новый уровень цен
    item1.pay_rate = 0.8
    # Применяем скидку
    item1.apply_discount()
    # Проверяет применилась ли цена с учётом нового уровня цен
    assert item1.price == 8000.0
    assert item2.price == 20000

    # Проверяет количество созданных классов
    assert Item.all == 2

    # Длина наименования товара меньше 10 символов
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'

    # Длина наименования товара больше 10 символов
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'


def test_item_csv():
    """Тестирование класса Item из src/item.py, служащего для представления товара в магазине. Получение данных из
    файла .csv"""

    # Создание объектов из данных файла
    Item.instantiate_from_csv('src/items.csv')

    # В файле 5 записей с данными по товарам
    assert len(Item.all) == 5

def test_item_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
