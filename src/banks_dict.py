import os
import re
from collections import Counter

# from src.utils import show_trans

transactions = [
    {
        "date": "2023-10-01",
        "description": "MASTERCARD PAYMENT TERMINAL",
        "amount": -1500.00,
        "currency": "RUB",
        "category": "Подписки",
    },
    {
        "date": "2023-10-02",
        "description": "APPLE.COM/BILL",
        "amount": -299.00,
        "currency": "USD",
        "category": "Подписки",
    },
    {
        "date": "2023-10-03",
        "description": "MASTERCARD CASHBACK",
        "amount": 50.50,
        "currency": "RUB",
        "category": "Возврат",
    },
    {
        "date": "2023-10-04",
        "description": "PYATEROCHKA STORE 123",
        "amount": -750.30,
        "currency": "RUB",
        "category": "Супермаркеты",
    },
    {
        "date": "2023-10-05",
        "description": "MASTERCARD PAYMENT TERMINAL",
        "amount": -1200.00,
        "currency": "RUB",
        "category": "Банковские услуги",
    },
]


def search_in_list(data: list, search: str) -> list:
    """Функция ищет словарь в списке который отвечает критериям поискового запроса в поле описание"""
    pattern = re.compile(search, re.IGNORECASE)
    # Пробуем генератор
    result = [x for x in data if pattern.search((x.get("description", "")))]
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Принимает список словарей с операциями и список с категориями операциями, возвращает словарь с количеством
    операций в списке словарей"""
    coincidence = []
    for x in data:
        for _ in categories:
            if x["description"] == _:
                coincidence.append(x["description"])
    counted = Counter(coincidence)
    result = dict(counted)
    return result


path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "operations.json"))
search_in_list(transactions, "executed")
