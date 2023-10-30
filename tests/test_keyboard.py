from pytest import raises

from src.keyboard import Keyboard


def test_keyboard():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    assert str(kb) == "Dark Project KD87A"

    # Проверка возможности изменить раскладку клавиатуры EN -> RU -> EN
    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang()
    assert str(kb.language) == "EN"

    # Проверка на отсутствие сеттера у атрибута language
    with raises(AttributeError):
        kb.language = 'CH'
