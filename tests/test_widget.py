import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "name, result", 
    [
        ("visa platinum 7000792289640636", "visa platinum 7000 79** **** 0636 "),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199 "),
        ("", "Введенные данные не являются банковскими реквизитами"),
        ("visa platinum 70001234792289640636", "visa platinum **0636"),
        ("Maestro 15968378687051991456", "Maestro **1456"),
        ("", "Введенные данные не являются банковскими реквизитами"),
    ],
)
def test_mask_account_card(name, result):
    assert mask_account_card(name) == result


@pytest.mark.parametrize("date, result", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2024-03-11", "11.03.2024")])
def test_get_date(date, result):
    assert get_date(date) == result
