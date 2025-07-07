import json

x = """
{
    "success": true,
    "query": {
        "from": "EUR",
        "to": "RUB",
        "amount": 43318.34
    },
    "info": {
        "timestamp": 1751832904,
        "rate": 92.831987
    },
    "date": "2025-07-06",
    "result": 4021327.575742
}
"""

print((json.loads(x))["result"])