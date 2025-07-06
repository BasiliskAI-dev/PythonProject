import json
import os
from dotenv import load_dotenv
import requests

load_dotenv()

operation12 = {

    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {
      "amount": "43318.34",
      "currency": {
        "name": "руб.",
        "code": "EUR"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160"
  }
def summ_trans(operation: dict) -> float:
    """Функция перевода валюта с помощью АПИ"""
    if operation["operationAmount"]["currency"]["code"] == "RUB":
        result = float(operation["operationAmount"]["amount"])
        return result
    else:
        api = os.getenv('API_KEY')
        headers = {
            "apikey": f"{api}"
        }
        from_param = operation["operationAmount"]["currency"]["code"]
        to_param = "RUB"
        summ = operation["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_param}&from={from_param}&amount={summ}"
        payload = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code

        result = (json.loads(response.text))["result"]
        return result

print(summ_trans(operation12))