import pytest

from src.masked import get_mask_card_number


@pytest.mark.parametrize("name, result", [('visa platinum 700079228960636', 'visa platinum 700 07** **** 0636 '), ('visa platinum 700079228960636', 'visa platinum 700 07** **** 0636 ')])
def test_get_mask_card_number(name, result):
    assert get_mask_card_number(name) == result


