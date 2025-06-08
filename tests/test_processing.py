import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import testdata_1, testdata_2, testdata_3


@pytest.mark.parametrize("input_data,expected_output", testdata_1)
def test_filter_by_state(input_data: list, expected_output: list) -> None:
    assert filter_by_state(input_data) == expected_output


def test_filter_by_state_raise() -> None:
    with pytest.raises(KeyError):
        filter_by_state([])


def test_filter_by_state_raise_key() -> None:
    with pytest.raises(KeyError):
        filter_by_state(testdata_3)


@pytest.mark.parametrize("input_data, output_expected", testdata_2)
def test_sort_by_date(input_data: list, output_expected: list) -> None:
    assert sort_by_date(input_data) == output_expected


def test_sort_by_date_raise() -> None:
    with pytest.raises(ValueError):
        sort_by_date([])
