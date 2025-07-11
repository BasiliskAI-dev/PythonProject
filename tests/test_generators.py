import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from tests.conftest import result_1, result_test_transaction_descriptions


def test_filter_by_currency(transactions_fixture):
    usd_transactions = list(filter_by_currency(transactions_fixture, "USD"))
    assert usd_transactions == result_1
    with pytest.raises(KeyError):
        valute = "USD"
        gen = (
            x for x in transactions_fixture if x.get("operationAmount", {})["curresdfancy"].get("code", None) == valute
        )
        next(gen)


def test_transaction_descriptions(transactions_fixture):
    descriptions = list(transaction_descriptions(transactions_fixture))
    assert descriptions == result_test_transaction_descriptions


def test_card_number_generator():
    gen = list(card_number_generator(1, 2))
    assert gen == ["0000 0000 0000 0001 "]
