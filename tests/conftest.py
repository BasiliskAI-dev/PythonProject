import pytest

from src.decorators import log

dict_1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "NOT-EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

dict_2 = [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]

testdata_1 = [
    (dict_1, dict_2),
]


test_state_input_1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

test_state_output_1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
test_state_input_2 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

test_state_output_2 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

testdata_2 = [
    (test_state_input_1, test_state_output_1),
    (test_state_input_2, test_state_output_2),
]

testdata_3 = [
    {"id": 41428829, "state": "", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "", "date": "2018-10-14T08:21:33.419441"},
]


@pytest.fixture
def transactions_fixture() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


result_1 = [
    {
        "date": "2018-06-30T02:08:58.425572",
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "id": 939719570,
        "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
        "state": "EXECUTED",
        "to": "Счет 11776614605963066702",
    },
    {
        "date": "2019-04-04T23:20:05.206878",
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "id": 142264268,
        "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
        "state": "EXECUTED",
        "to": "Счет 75651667383060284188",
    },
    {
        "date": "2018-08-19T04:27:37.904916",
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "id": 895315941,
        "operationAmount": {"amount": "56883.54", "currency": {"code": "USD", "name": "USD"}},
        "state": "EXECUTED",
        "to": "Visa Platinum 8990922113665229",
    },
]


result_test_filter_by_currency = {
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188",
}

result_test_transaction_descriptions = [
    "Перевод организации",
    "Перевод со счета на счет",
    "Перевод со счета на счет",
    "Перевод с карты на карту",
    "Перевод организации",
]

transactions_empty: list = []


@log()
def get_mask_card_number(full_name: str) -> str:
    """Принимает номер карты, возвращает номер карты со скрытыми числами"""
    card_letters = full_name[:-16]
    card_numbers = ""
    for item in full_name:
        if item.isdigit():
            card_numbers += item
    if len(card_numbers) != 16:
        result = "Введен некорректный номер карты"
        raise ValueError(result)
    else:
        card_number_hidden = ""
        for number in range(0, len(card_numbers), 4):
            card_number_hidden += card_numbers[number : number + 4] + " "
        result = card_letters + card_number_hidden[0:7] + "** **** " + card_number_hidden[-5:]
        print(result)

    return result


@log("log")
def get_mask_card_number_file(full_name: str) -> str:
    """Принимает номер карты, возвращает номер карты со скрытыми числами"""
    card_letters = full_name[:-16]
    card_numbers = ""
    for item in full_name:
        if item.isdigit():
            card_numbers += item
    if len(card_numbers) != 16:
        result = "Введен некорректный номер карты"
        raise ValueError(result)
    else:
        card_number_hidden = ""
        for number in range(0, len(card_numbers), 4):
            card_number_hidden += card_numbers[number : number + 4] + " "
        result = card_letters + card_number_hidden[0:7] + "** **** " + card_number_hidden[-5:]
        print(result)

    return result


# get_mask_card_number_file("visa platinum 700079228960636115656")


operation12 = {
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "EUR"}},
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160",
}

operation12_RUB = {
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "EUR"}},
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160",
}

json_response = """
{
    "success": true,
    "query": {
        "from": "EUR",
        "to": "RUB",
        "amount": 43318.34
    },
    "info": {
        "timestamp": 1751832904,
        "rate": 92.831987
    },
    "date": "2025-07-06",
    "result": 4021327.575742
}
"""
