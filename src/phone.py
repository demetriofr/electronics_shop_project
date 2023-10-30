from src.item import Item


class Phone(Item):
    """
    Класс для представления конкретного товара телефон в магазине
    """

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        # количество поддерживаемых сим-карт
        self.number_of_sim = number_of_sim

    @classmethod
    def verify_number_of_sim(cls, number_of_sim):
        """
        Проверяет чтобы имя было целым числом и больше нуля
        """
        if type(number_of_sim) == int and number_of_sim > 0:
            return number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        number_of_sim = self.verify_number_of_sim(number_of_sim)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """
        Выводит информацию о классе и аттрибутах класса, включая количество сим-карт.
        """
        return super().__repr__()[:-1] + f", {self.number_of_sim})"
