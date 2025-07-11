import logging
import os

app_logger = logging.getLogger('logging for utils')
path_to_log = os.path.join("..", "logs", "logs.log")
file_handler = logging.FileHandler(path_to_log, mode='w', encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)


def get_mask_card_number(full_name: str) -> str:
    """Принимает номер карты, возвращает номер карты со скрытыми числами"""
    app_logger.info('Программа запустилась')
    card_letters = full_name[:-16]
    card_numbers = ""
    app_logger.info('Началось формирование номера')
    for item in full_name:
        if item.isdigit():
            card_numbers += item
    if len(card_numbers) != 16:
        result = "Введен некорректный номер карты"
        app_logger.critical('Номер может содержать лишь 16 цифр')
        raise ValueError(result)
    else:
        app_logger.info('Программа отработала корректно, шифруется номер и название карты')
        card_number_hidden = ""
        for number in range(0, len(card_numbers), 4):
            card_number_hidden += card_numbers[number : number + 4] + " "
        result = card_letters + card_number_hidden[0:7] + "** **** " + card_number_hidden[-5:]
        print(result)
        app_logger.info('Программа закончила свою работу')
    return result


def get_mask_account(full_name: str) -> str:
    """Принимает номер аккаунта, возвращает номер аккаунта со
    скрытыми цифрами"""
    app_logger.info('Программа запустилась')
    account_number = ""
    app_logger.info('Началось формирование номера аккаунта')
    for item in full_name:
        if item.isdigit():
            account_number += item
    if len(account_number) != 20:
        result = "Введен некорректный номер аккаунта"
        app_logger.critical('Номер может содержать лишь 20 цифр')
        raise ValueError(result)
    else:
        app_logger.info('Программа отработала корректно, шифруется номер аккаунта')
        account_letters = full_name[:-20]
        result = account_letters + "**" + account_number[-4:]
        print(result)
        app_logger.info('Программа закончила свою работу')
    return result

get_mask_account("16554567458749654213")