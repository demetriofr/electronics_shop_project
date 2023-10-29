from src.item import Item


class Phone(Item):
    """
    Класс для представления конкретного товара телефон в магазине
    """
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        # количество поддерживаемых сим-карт
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """
        Выводит информацию о классе и аттрибутах класса, включая количество сим-карт.
        """
        return super().__repr__()[:-1] + f", {self.number_of_sim})"
