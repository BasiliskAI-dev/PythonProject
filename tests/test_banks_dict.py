from src.banks_dict import process_bank_operations, search_in_list

# Тестовые данные
test_transactions = [
    {"description": "Payment to Bank A", "amount": 100},
    {"description": "Transfer to Card 1234", "amount": 200},
    {"description": "Bank B deposit", "amount": 300},
    {"description": "Payment to Bank C", "amount": 400},
]


def test_search_in_list():
    """Тест поиска по описанию"""
    result = search_in_list(test_transactions, "Bank")
    assert len(result) == 3  # Найдено 3 транзакции

    result = search_in_list(test_transactions, "Card")
    assert len(result) == 1
    assert result[0]["amount"] == 200


def test_process_bank_operations():
    """Тест подсчёта операций по категориям"""
    categories = ["Payment to Bank A", "Bank B deposit"]
    result = process_bank_operations(test_transactions, categories)

    assert result == {"Payment to Bank A": 1, "Bank B deposit": 1}
