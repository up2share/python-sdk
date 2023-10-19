import pytest
from u2s_sdk.client import ApiClient
from u2s_sdk.handler import ResumableUploadHandler

@pytest.fixture
def client(mocker):
    return ApiClient(base_url='https://test-api.com')

def test_start_upload_successful(client, mocker):
    # Mock the post method of the ApiClient to simulate a successful start_upload request
    mocker.patch.object(client, 'post', return_value=mocker.Mock(status_code=201, headers={'Location': '/upload?key=123'}))

    handler = ResumableUploadHandler(client)
    location_uri, upload_key = handler.start_upload('test.txt', 1024)

    assert location_uri == '/upload?key=123'
    assert upload_key == '123'

def test_start_upload_failed(client, mocker):
    # Mock the post method of the ApiClient to simulate a failed start_upload request
    mocker.patch.object(client, 'post', return_value=mocker.Mock(status_code=400))

    handler = ResumableUploadHandler(client)

    with pytest.raises(Exception, match=r'Failed to initiate resumable upload\. Status code: 400'):
        handler.start_upload('test.txt', 1024)

def test_upload_chunk_successful(client, mocker):
    # Mock the put method of the ApiClient to simulate a successful upload_chunk request
    mocker.patch.object(client, 'put', return_value=mocker.Mock(status_code=201, headers={}))

    handler = ResumableUploadHandler(client)
    response_headers = handler.upload_chunk('/upload?key=123', 4, b'data', 0, 3)

    assert response_headers == {}

def test_upload_chunk_in_progress(client, mocker):
    # Mock the put method of the ApiClient to simulate an in-progress upload_chunk request
    mocker.patch.object(client, 'put', return_value=mocker.Mock(status_code=308))

    handler = ResumableUploadHandler(client)
    response_headers = handler.upload_chunk('/upload?key=123', 4, b'data', 0, 2)

    assert response_headers is False

def test_upload_chunk_failed(client, mocker):
    # Mock the put method of the ApiClient to simulate a failed upload_chunk request
    mocker.patch.object(client, 'put', return_value=mocker.Mock(status_code=400))

    handler = ResumableUploadHandler(client)

    with pytest.raises(Exception, match=r'Failed to upload chunk\. Status code: 400'):
        handler.upload_chunk('/upload?key=123', 1024, b'data', 0, 3)

# Add more test cases for the ResumableUploadHandler class as needed
