import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def converter(operation: dict) -> float:
    """Функция перевода валюта с помощью АПИ"""
    if operation["operationAmount"]["currency"]["code"] == "RUB":
        result = float(operation["operationAmount"]["amount"])
        return result
    else:
        api = os.getenv("API_KEY")
        headers = {"apikey": f"{api}"}
        from_param = operation["operationAmount"]["currency"]["code"]
        to_param = "RUB"
        summ = operation["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_param}&from={from_param}&amount={summ}"
        payload = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        result = (json.loads(response.text))["result"]
        return result
