from functools import wraps
from typing import Any


def log(filename=""):
    def inner(func):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            if bool(filename):
                try:
                    with open(f"{filename}.txt", "a", encoding="utf-8") as file:
                        file.write(f"Вызов функции {func.__name__} с аргументами: args={args}, kwargs={kwargs}\n")
                    result = func(*args, **kwargs)
                    with open(f"{filename}.txt", "a", encoding="utf-8") as file:
                        file.write(f"Функция {func.__name__} вернула: {result}\n")
                    return result
                except Exception as e:
                    with open(f"{filename}.txt", "a", encoding="utf-8") as file:
                        file.write(f"Ошибка в {func.__name__}: {e}")
                    raise Exception
            else:
                try:
                    print(f"Вызов функции {func.__name__} с аргументами: args={args}, kwargs={kwargs}\n")
                    result = func(*args, **kwargs)
                    print(f"Функция {func.__name__} вернула: {result}\n")
                    return result
                except Exception as e:
                    print(f"Ошибка в {func.__name__}: {e}")
                    raise Exception

        return wrapper

    return inner
