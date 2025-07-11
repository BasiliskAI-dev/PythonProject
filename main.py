from src.generators import card_number_generator
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

card_number = "visa platinum 7000792289606361"
account_number = "Счет 73654108430135874305"
date = "2024-03-11T02:26:18.671407"

mask_account_card(card_number)
mask_account_card(account_number)
get_date(date)

info_account1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

filter_by_state(info_account1, "CANCELED")

info_account2 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

sort_by_date(info_account2)

for card_number in card_number_generator(5, 10):
    print(card_number)
