from unittest.mock import patch

import pytest
from requests import Response

from src.api import HH


@patch("requests.get")
def test_api_connect_success(mock_request_get, hh_api):
    sample_response = Response()
    mock_request_get.return_value = sample_response
    mock_request_get.return_value.status_code = 200
    result = hh_api._api_connect("Python")
    assert result == sample_response


@patch("requests.get")
def test_api_connect_fail(mock_request_get, hh_api):
    sample_response = Response()
    mock_request_get.return_value = sample_response
    mock_request_get.return_value.status_code = 404
    with pytest.raises(ValueError):
        hh_api._api_connect("Python")


@patch.object(HH, "_api_connect")
def test_api_load_vacancies(mock_api_connect, hh_api):
    mock_api_connect.return_value.json.return_value = {"items": [{"id": 1}, {"id": 2}]}
    result = hh_api.load_vacancies()
    assert result == [
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
        {"id": 1},
        {"id": 2},
    ]
