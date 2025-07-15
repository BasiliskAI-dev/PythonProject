import json
import logging
import os


def show_trans(path: str) -> list:
    """Функция отображает лист с транзакциями"""
    app_logger = logging.getLogger("logging for utils")
    path_to_log = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs", "logs.log"))
    file_handler = logging.FileHandler(path_to_log, mode="w", encoding="utf-8")
    file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    app_logger.addHandler(file_handler)
    app_logger.setLevel(logging.DEBUG)
    try:
        app_logger.debug("Запуск приложения")
        if os.path.getsize(path) == 0:
            app_logger.warning("Файл пустой. Вернул пустой список")
            return []
        else:
            app_logger.debug("Попытка прочесть файл")
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)
                # Проверяю в файле есть список или нет?
                app_logger.info("Файл прочитан")
                if isinstance(data, list):
                    app_logger.debug("Успешно, функция прочла файл. Функция вернула значение")
                    return data
                else:
                    app_logger.warning("В файле нет необходимых объектов")
                    return []
    except FileNotFoundError:
        app_logger.critical("ОШИБКА! Файл не найден в директории. Проверьте директорию")
        return []
