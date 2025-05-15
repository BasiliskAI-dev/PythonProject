from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(many_numbers: str) -> None:
    key_word = "Счет"
    if 'key_word' in many_numbers:
        get_mask_account(many_numbers)
    else:
        get_mask_card_number(many_numbers)

    return None