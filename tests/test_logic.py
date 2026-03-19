from pytest import raises

from app.logic import is_windy_day
from app.logic import URL



def test_is_windy_true(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {
        'current_weather': {
            'windspeed': 5
        } 
    }
    mock_get = mocker.patch('app.logic.requests.get', return_value=mock_response)
    result = is_windy_day()

    assert result is False
 
    mock_get.assert_called_once_with(URL)


def test_is_windy_raise_error(mocker):
    mock_get = mocker.patch('app.logic.requests.get', side_effect=ConnectionError('No Internet'))
    with raises(ConnectionError) as excinfo:
        is_windy_day()
    assert 'No Internet' in str(excinfo.value)
    mock_get.assert_called_once_with(URL)


def test_with_monkeypatch(monkeypatch):
    class MockResponse:
        def json(*args, **kwargs):
            return {'current_weather': { 'windspeed': '10.5', }, }

    import requests
    monkeypatch.setattr(requests, 'get', lambda url: MockResponse())
    response = is_windy_day()
    assert response is True