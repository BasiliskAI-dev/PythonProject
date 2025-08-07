import os
from unittest.mock import patch

from CONSTANCE import PATH_TO_FILE_OPERATIONS
from src.utils import show_trans


@patch("json.load")
def test_show_trans(mock_change):
    data = [1, 2, 3]
    mock_change.return_value = data
    assert show_trans(PATH_TO_FILE_OPERATIONS) == data


def test_empty_file():
    test_path = os.path.join(os.path.dirname(__file__), "tests", "empty_file_for_test.json")
    assert show_trans(test_path) == []


def test_show_trans_dict():
    test_path = os.path.join(os.path.dirname(__file__), "tests", "dict_for_test.json")
    assert show_trans(test_path) == []


def test_show_trans_fnf():
    test_path = os.path.join(os.path.dirname(__file__), "tests", "dict_for_teeeeest.json")
    assert show_trans(test_path) == []
