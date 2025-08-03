import pytest
# from lesson import get_weather
from lesson import get_github_user
# # Настраиваем моки
# def test_get_weather(mocker):
#     mock_get = mocker.patch('lesson.requests.get') # Подменяем requests.get на мок
#     mock_get.return_value.status_code = 200 # Мок возвращает статус 200
#     mock_get.return_value.json.return_value = { # Мок возвращает данные
#         'weather': [{
#             'temp': 20.0,
#             'feels_like': 18.0,
#             'description': 'clear sky'
#         }]
#     }
#     # Запускаем тест
#     api_key = '92614399a18da57057e083f734235ecd'
#     city = 'New York'
#     weather_data = get_weather(api_key, city) # Вызываем функцию
#     # Проверяем результат
#     assert weather_data == {'weather': [{'temp': 20.0, 'feels_like': 18.0, 'description': 'clear sky'}]}
#
# def test_get_weather_error(mocker):
#     mock_get = mocker.patch('lesson.requests.get') # Подменяем requests.get на мок
#     mock_get.return_value.status_code = 404 # Мок возвращает статус 404
#     # Запускаем тест
#     api_key = '92614399a18da57057e083f734235ecd'
#     city = 'New York'
#     weather_data = get_weather(api_key, city) # Вызываем функцию
#     # Проверяем результат
#     assert weather_data is None


def test_get_github_user(mocker):
    mock_get = mocker.patch('lesson.requests.get')  # Подменяем requests.get на мок
    mock_get.return_value.status_code = 200  # Мок возвращает статус 200
    mock_get.return_value.json.return_value = {  # Мок возвращает данные
        'name': 'John Doe',
        'location': 'New York'
    }
    # Запускаем тест
    # username = 'johndoe'
    github_data = get_github_user('username')  # Вызываем функцию
    # Проверяем результат
    assert github_data == {'name': 'John Doe', 'location': 'New York'}

def test_get_github_user_error(mocker):
    mock_get = mocker.patch('lesson.requests.get')  # Подменяем requests.get на мок
    mock_get.return_value.status_code = 404  # Мок возвращает статус 404
    # Запускаем тест
    # username = 'johndoe'
    github_data = get_github_user('username')  # Вызываем функцию
    # Проверяем результат
    assert github_data is None