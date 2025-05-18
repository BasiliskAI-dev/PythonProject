from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(full_name: str) -> None:
    count=''
    for symbol in full_name:
        if symbol.isdigit():
            count+=symbol
    if len(count) == 20:
        get_mask_account(full_name)
    else:
        get_mask_card_number(full_name)

    return None