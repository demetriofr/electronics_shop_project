from src.item import Item


def test_csv_not_found_error():
    # Файл items.csv отсутствует.
    assert Item.instantiate_from_csv('src/not_found.csv') == 'FileNotFoundError: Отсутствует файл item.csv'


def test_instantiate_csv_error():
    # В файле items.csv удалена последняя колонка.
    assert str(Item.instantiate_from_csv('tests/items_err.csv')) == 'InstantiateCSVError: Файл item.csv поврежден'
