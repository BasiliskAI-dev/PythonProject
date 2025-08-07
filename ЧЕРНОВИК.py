# from src.widget import get_date
#
# dict = [{"id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {"amount": "31957.58","currency": {"name": "руб.", "code": "RUB"}},
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   },
#         {"id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {"amount": "31957.58","currency": {"name": "руб.", "code": "RUB"}},
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"}
# ]
#
# for x in dict:
#     hui = get_date(x['date'])
#     print(f'Получилось?{hui}')
import os

from src.banks_dict import search_in_list
from src.utils import show_trans

path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "data", "operations.json"))
res = show_trans(path2)
# print(res)
# print(search_in_list(res, 'Открытие вклада'))
for x in res:
    # print(x.get('description', ''), x.get('from', ''), x.get('to', ''))
    print(x)
print(len(res))
# dictator = {'id': 587085106,
#  'state': 'EXECUTED',
#  'date': '2018-03-23T10:45:06.972075',
#  'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
#  'description': 'Открытие вклада',
#  'to': 'Счет 41421565395219882431'}