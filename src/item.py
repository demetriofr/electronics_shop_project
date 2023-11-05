import os.path
from csv import DictReader

from src.csverror import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = 0
    PATH_NAME = 'src/items.csv'

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

        self.all += 1

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @classmethod
    def verify_name(cls, name):
        """
        Имя должно быть не больше 10 символов
        """
        return name[:10]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        name = self.verify_name(name)
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls, path_name=PATH_NAME):
        """
        Создаёт объекты из данных файла .csv
        """

        items = []
        path_name = str(cls.path_file(path_name))

        try:
            with open(path_name, newline='', encoding='windows-1251') as csv_f:
                reader = DictReader(csv_f)
                if reader.fieldnames != ['name', 'price', 'quantity']:
                    raise InstantiateCSVError
                for row in reader:
                    name = str(row['name'])
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    item = cls(name, price, quantity)
                    items.append(item)
                cls.all += len(items)
        except FileNotFoundError:
            err_text = 'FileNotFoundError: Отсутствует файл item.csv'
            print(err_text)
            return err_text
        except InstantiateCSVError as err:
            print(err)
            return err

    @staticmethod
    def path_file(path_name):
        """
        Создаёт путь для файла при условии, что файл лежит в другой папке родительского каталога

        :param path_name: путь к файлу в подобном формате 'src/items.csv'
        """
        path_list = path_name.split('/')
        path_file = os.path.join('..', path_list[0], path_list[1])
        return path_file

    @staticmethod
    def string_to_number(string):
        string.split('.')
        return int(string[0])

    def __repr__(self):
        """
        Выводит информацию о классе и атрибутах класса.
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
        # return f"{self.__class__.__name__}('{str(self.__dict__.values())[14:-2]})"  # Не очень наглядно, но эффективно

    def __str__(self):
        """
        Выводит информацию об атрибуте название товара
        """
        return f"{self.name}"

    def __add__(self, other):
        """
        Складывает атрибут количество товара (quantity)
        класса Item и (или) его дочерних классов
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        else:
            raise ValueError('Складываться должны атрибуты quantity класса Item и (или) его дочерних классов')
