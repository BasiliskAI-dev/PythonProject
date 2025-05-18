from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(full_name: str) -> None:
    key_word = "Счет"
    if 'key_word' in full_name:
        get_mask_account(full_name)
    else:
        get_mask_card_number(full_name)

    return None