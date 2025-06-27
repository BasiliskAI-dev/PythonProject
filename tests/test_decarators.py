import pytest

from tests.conftest import get_mask_card_number, get_mask_card_number_file


def test_log_console(capsys):
    get_mask_card_number("visa platinum 7000792289606361")
    captured = capsys.readouterr()
    assert captured.out == (
        "Вызов функции get_mask_card_number с аргументами: args=('visa platinum "
        "7000792289606361',), kwargs={}\n"
        "\n"
        "visa platinum 7000 79** **** 6361 \n"
        "Функция get_mask_card_number вернула: visa platinum 7000 79** **** 6361 \n"
        "\n"
    )


def test_log_console_error(capsys):
    with pytest.raises(ValueError, match="Введен некорректный номер карты"):
        get_mask_card_number("visa platinum 700079228960636115656")


def test_log_file():
    get_mask_card_number_file("asdfasfd sd s 1654564616541654")
    file = open("log.txt", "r", encoding="utf-8")
    content = file.read()
    assert content == (
        "Вызов функции get_mask_card_number_file с аргументами: args=('asdfasfd sd s "
        "1654564616541654',), kwargs={}\n"
        "Функция get_mask_card_number_file вернула: asdfasfd sd s 1654 56** **** "
        "1654 \n"
    )
    with open("log.txt", "w") as file:
        file.truncate(0)  # Очищает файл


def test_log_file_error():
    with pytest.raises(ValueError, match="Введен некорректный номер карты"):
        get_mask_card_number("visa platinum 700079228960636115656")
        file = open("log.txt", "r", encoding="utf-8")
        content = file.read()
        assert (
            content
            == """Вызов функции get_mask_card_number_file с аргументами: args=('visa platinum 700079228960636115656',), kwargs={}
Ошибка в get_mask_card_number_file: Введен некорректный номер карты"""
        )
        file.truncate(0)
