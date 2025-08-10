import json
import os
from unittest.mock import Mock, patch

from dotenv import load_dotenv

from src.external_api import converter

load_dotenv()


@patch("src.external_api.requests.request")
def test_converter_usd(mock_request):
    fake_response = Mock()
    fake_response.text = json.dumps({"result": 4500.0})
    mock_request.return_value = fake_response
    operation = {"operationAmount": {"amount": "50.0", "currency": {"code": "USD"}}}
    result = converter(operation)
    assert result == 4500.0
    api = os.getenv("API_KEY")
    mock_request.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=50.0",
        headers={"apikey": f"{api}"},
        data={},
    )


def test_converter_rub():
    operation = {"operationAmount": {"amount": "50.0", "currency": {"code": "RUB"}}}
    assert converter(operation) == 50
