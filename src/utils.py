import json
import os

from CONSTANCE import PATH_TO_FILE_OPERATIONS


def show_trans(path: str) -> list:
    """Функция отображает лист с транзакциями"""
    try:
        if os.path.getsize(path) == 0:
            return []
        else:
            with open(path, "r", encoding='utf-8') as file:
                data = json.load(file)
                #Проверяю в файле есть список или нет?
                if isinstance(data, list):
                    return data
                else:
                    return []
    except FileNotFoundError:
        return []




print(show_trans(PATH_TO_FILE_OPERATIONS))