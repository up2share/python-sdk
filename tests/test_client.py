import pytest
from u2s_sdk.client import ApiClient
import requests.exceptions

@pytest.fixture
def client(mocker):
    return ApiClient(base_url='https://test-api.com')

def test_get_headers_no_auth(client):
    headers = client.get_headers()
    assert 'X-Api-Key' not in headers
    assert 'Authorization' not in headers

def test_get_headers_api_key():
    client = ApiClient(base_url='https://test-api.com', api_key='test_key')
    headers = client.get_headers()
    assert headers['X-Api-Key'] == 'test_key'
    assert 'Authorization' not in headers

def test_get_headers_oauth_token():
    client = ApiClient(base_url='https://test-api.com', oauth_token='test_token')
    headers = client.get_headers()
    assert 'X-Api-Key' not in headers
    assert headers['Authorization'] == 'Bearer test_token'

def test_get_request_successful(client, mocker):
    # Mock the requests.get method
    mock_get = mocker.patch('requests.get')
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    response = client.get('/test')
    assert response.status_code == 200

def test_get_request_exception(client, mocker):
    # Mock the requests.get method to raise an exception
    mocker.patch('requests.get', side_effect=requests.exceptions.RequestException('Test error'))

    response = client.get('/test')
    assert response is None
