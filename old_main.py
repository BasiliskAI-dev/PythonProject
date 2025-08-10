# from src.generators import card_number_generator
# from src.processing import filter_by_state, sort_by_date
# from src.widget import get_date, mask_account_card
#
# card_number = "visa platinum 7000792289606361"
# account_number = "Счет 73654108430135874305"
# date = "2024-03-11T02:26:18.671407"
#
# mask_account_card(card_number)
# mask_account_card(account_number)
# get_date(date)
#
# info_account1 = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
# ]
#
# filter_by_state(info_account1, "CANCELED")
#
# info_account2 = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
#
# sort_by_date(info_account2)
#
# for card_number in card_number_generator(5, 10):
#     print(card_number)

from src.banks_dict import search_in_list
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.readers import csv_reader, excel_reader
from src.utils import show_trans
from src.widget import get_date, mask_account_card


def main(file):
    print(
        """Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )
    menu_options = {"1": show_trans, "2": csv_reader, "3": excel_reader}

    while True:
        user_input = input("Введите цифру: ")

        if user_input in menu_options:
            result_reader = menu_options[user_input](file)
            if user_input == "1":
                print("Для обработки выбран JSON-файл")
            elif user_input == "2":
                print("Для обработки выбран CSV-файл")
            elif user_input == "3":
                print("Для обработки выбран XLSX-файл")
            break
        else:
            print("Введите число от 1 до 3")

    print(
        """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    )

    while True:
        user_input = input("Введите статус: ").upper()
        if user_input == "EXECUTED" or user_input == "CANCELED" or user_input == "PENDING":
            result = filter_by_state(result_reader, user_input)
            break
        else:
            print("Введите корректный статус")
    while True:
        need_date = input("Отсортировать операции по дате? Да/Нет:").lower()
        if need_date == "да" or need_date == "нет":
            if need_date == "да":
                while True:
                    reverse_date = input(
                        "Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию:"
                    ).lower()
                    if reverse_date == "по возрастанию":
                        result = sort_by_date(result, True)
                        break
                    elif reverse_date == "по убыванию":
                        result = sort_by_date(result, False)
                        break
                    else:
                        print("ПО ВОЗРАСТАНИЮ ИЛИ ПО УБЫВАНИЮ!!!")
            elif need_date == "нет":
                break
            break
        else:
            print('Мне нужно лишь "да" или "нет"')
    while True:
        ruble_trans = input("Выводить только рублевые транзакции? Да/Нет:").lower()
        if ruble_trans == "да" or ruble_trans == "нет":
            if ruble_trans == "да":
                result = list(filter_by_currency(result, "RUB"))
                break
        else:
            print('Мне нужно лишь "да" или "нет"')

    while True:
        description_trans = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет:").lower()
        if description_trans == "да" or description_trans == "нет":
            if description_trans == "да":
                us_inp = input("Введите слово для фильтрации:")
                result = search_in_list(result, us_inp)
                break
        else:
            print('Мне нужно лишь "да" или "нет"')

    if result == []:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    res_len = len(result)

    print(f"Нашлось {res_len} совпадений")

    for x in result:
        date_result = get_date(x.get("date"))
        from_field = mask_account_card(x.get("from"))
        to_field = mask_account_card(x.get("to"))
        amount_field = x.get("operationAmount").get("amount")
        if "ткрытие" in x.get("description"):
            result_x = f"""
{date_result} {x.get('description')}
{to_field}
Сумма: {amount_field}
"""
            print(result_x)
        else:
            result_x = f"""
{date_result} {x.get('description')}
{from_field} -> {to_field}
Сумма: {amount_field}
"""
            print(result_x)

main("data/operations.json")