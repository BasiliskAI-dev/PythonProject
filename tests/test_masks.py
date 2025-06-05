import pytest

from src.widget import *


@pytest.mark.parametrize("name, result", [('visa platinum 7000792289640636', 'visa platinum 7000 79** **** 0636 '),
                                          ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199 '),
                                          ('', 'Введен некорректный номер карты')])

def test_get_mask_card_number(name, result):
    assert get_mask_card_number(name) == result


@pytest.mark.parametrize("name, result", [('visa platinum 70001234792289640636', 'visa platinum **0636'),
                                          ('Maestro 15968378687051991456', 'Maestro **1456'),
                                          ('', 'Введен некорректный номер аккаунта')])

def test_get_mask_account(name, result):
    assert get_mask_account(name) == result

@pytest.mark.parametrize('name, result', [('visa platinum 7000792289640636', 'visa platinum 7000 79** **** 0636 '),
                                          ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199 '),
                                          ('', 'Введенные данные не являются банковскими реквизитами'),
                                          ('visa platinum 70001234792289640636', 'visa platinum **0636'),
                                          ('Maestro 15968378687051991456', 'Maestro **1456'),
                                          ('', 'Введенные данные не являются банковскими реквизитами')]
                         )

def test_mask_account_card(name, result):
    assert mask_account_card(name) == result

