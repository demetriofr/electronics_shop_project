from src.item import Item


class KeyboardLayout:
    """
    Класс для изменения раскладки клавиатуры
    """

    def __init__(self, language='EN'):
        self.verify_language(language)
        self.__language = language

    @classmethod
    def verify_language(cls, language):
        if language != 'EN' and language != 'RU':
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
        else:
            return language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self.__language
        else:
            self.__language = 'EN'
            return self.__language


class Keyboard(Item, KeyboardLayout):
    """
    Класс для представления клавиатур (конкретного товара) в магазине
    """

    def __init__(self, name, price, quantity):
        self._name = name
        super().__init__(name, price, quantity)

    def __str__(self):
        """
        Выводит информацию об атрибуте название товара
        """
        return f"{self._name}"
