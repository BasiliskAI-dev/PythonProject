from unittest.mock import mock_open, patch

import pandas as pd

from src.readers import csv_reader, excel_reader


def test_cvs_reader():
    with patch("builtins.open", mock_open(read_data="что-то на иврите")):
        assert csv_reader("any") == []


def test_excel_reader():
    mock_data = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})

    with patch("pandas.read_excel") as mock_reader:
        mock_reader.return_value = mock_data
        result = excel_reader("aaa.xlsx")
        assert result == [{"Name": "Alice", "Age": 25}, {"Name": "Bob", "Age": 30}]
        mock_reader.assert_called_once_with("aaa.xlsx")
