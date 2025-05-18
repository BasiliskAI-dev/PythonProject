from masks import get_mask_account, get_mask_card_number


def mask_account_card(full_name: str) -> None:
    """Функция решает какую далее использовать функцию"""

    count = ''
    for symbol in full_name:
        if symbol.isdigit():
            count += symbol
    if len(count) == 20:
        get_mask_account(full_name)
    else:
        get_mask_card_number(full_name)

    return None


def get_date(date: str) -> str:
    """Возвращает короткую версию даты"""

    short_date = date[8:10] + '.' + date[5:7] + '.' + date[0:4]
    print(short_date)
    return short_date
