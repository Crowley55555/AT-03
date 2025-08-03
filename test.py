import pytest
from main import get_cats


def test_get_cats(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {'id': 1,
         'name': 'test',
         'url': 'https://cdn2.thecatapi.com/images/abc123.jpg'
         }]
    assert get_cats() == [
        {'id': 1,
         'name': 'test',
         'url': 'https://cdn2.thecatapi.com/images/abc123.jpg'
         }]

def test_get_cats_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404
    assert get_cats() is None