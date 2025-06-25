import pytest

from src.masked import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "name, result",
    [
        ("visa platinum 7000792289640636", "visa platinum 7000 79** **** 0636 "),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199 "),
    ],
)
def test_get_mask_card_number(name: str, result: str) -> None:
    assert get_mask_card_number(name) == result


@pytest.mark.parametrize(
    "name, result",
    [
        ("visa platinum 70001234792289640636", "visa platinum **0636"),
        ("Maestro 15968378687051991456", "Maestro **1456"),
    ],
)
def test_get_mask_account(name: str, result: str) -> None:
    assert get_mask_account(name) == result


def test_mask_card_raise() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_get_mask_account_raise() -> None:
    with pytest.raises(ValueError):
        get_mask_account("")
