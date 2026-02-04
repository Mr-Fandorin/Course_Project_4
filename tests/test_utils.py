import json
from unittest.mock import patch

from src.utils import JSONFileWorker


def test_get_data(fileworker):
    result = fileworker.get_data()
    assert result == [{"name": "John Doe", "age": 30, "email": "johndoe@example.com"}]


@patch.object(JSONFileWorker, "get_data")
def test_save_data(mock_get_data, fileworker):
    fileworker.filename = "tests/test_file_2.json"
    new_data = [{"url": 5}, {"url": 2}, {"url": 6}, {"url": 7}]
    mock_get_data.return_value = [{"url": 1}, {"url": 2}, {"url": 3}, {"url": 4}]
    fileworker.save_data(new_data)

    with open("tests/test_file_2.json", "r") as f:
        result = json.load(f)
        assert result == [{"url": 1}, {"url": 2}, {"url": 3}, {"url": 4}, {"url": 5}, {"url": 6}, {"url": 7}]


def test_file_delete(fileworker_2):
    fileworker_2.file_delete()
    with open(fileworker_2.filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data == []
