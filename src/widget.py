from datetime import datetime

from src.masked import get_mask_account, get_mask_card_number


def mask_account_card(full_name: str) -> str:
    """Функция решает какую далее использовать функцию"""

    count = ""
    for symbol in full_name:
        if symbol.isdigit():
            count += symbol
    if len(count) == 20:
        result = get_mask_account(full_name)
    elif len(count) == 16:
        result = get_mask_card_number(full_name)
    else:
        result = "Введенные данные не являются банковскими реквизитами"

    return result


def get_date(date: str) -> str:
    """Возвращает короткую версию даты"""

    # short_date = date[8:10] + "." + date[5:7] + "." + date[0:4]
    short_date = datetime.fromisoformat(date)
    return short_date.strftime("%d.%m.%Y")
