from typing import Any, Generator


def filter_by_currency(transactions: list, valute: str) -> Generator[Any, Any, None] or str:
    """Возвращает словарь из списка transactions по коду valute"""
    gen = (
        x
        for x in transactions
        if x.get("operationAmount", {}).get("currency", {}).get("code", None) == valute
        or x.get("currency_code") == valute
    )
    return gen


def transaction_descriptions(transactions: list) -> Generator[Any, Any, None]:
    """Возвращает описание переводов из списка transactions"""
    gen = (x["description"] for x in transactions if "description" in x)
    return gen


def card_number_generator(start: int, stop: int) -> Generator[Any, Any, None]:
    """Возвращает номер карты в диапазоне от start до stop"""
    default_number = 10000000000000000 + start
    for x in range(start, stop):
        new_number = ""
        str_default_number = str(default_number)[1:]
        for _ in range(0, len(str_default_number), 4):
            new_number += str_default_number[_ : _ + 4] + " "
        yield new_number
        default_number += 1
