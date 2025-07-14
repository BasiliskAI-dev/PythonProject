import csv
import pandas as pd
import os
import openpyxl


def cvs_reader(path: str)->list:
    """Читает файл csv и возвращает список"""
    with open(path, 'r', encoding="utf-8") as file:
        reader = pd.read_csv(file, delimiter=';')
        df = reader.to_dict("records")
        return df

# path1 = (os.path.join(os.path.dirname(__file__), '..', "data", "transactions.csv")
# print(cvs_reader(path1))

def excel_reader(path: str) -> list:
    reader = pd.read_excel(path)
    reader_to_dict = reader.to_dict("records")
    return reader_to_dict

path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "data", "transactions_excel.xlsx"))
print(excel_reader(path2))