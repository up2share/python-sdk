"""
Handler module.

u2s_sdk.handler
"""
import os
import json

from .utils import get_key_value_from_uri
from .client import ApiClient


class ResumableUploadHandler:
    """
    Resumable upload handler.
    """

    def __init__(self, api_client: ApiClient):
        """
        Constructor.

        :param api_client: The API client
        """
        self.api_client = api_client
        self.logger = api_client.get_logger()

    def start_upload(self, filename: str, total_size: int, content_type='application/octet-stream'):
        """
        Start a resumable upload.

        :param filename: The filename
        :param total_size: The total file size (in bytes)
        :param content_type: The content type (default: application/octet-stream)
        :return: The upload URI and the upload key
        """
        headers = {
            'Content-Type': content_type,
            'X-Upload-Content-Length': str(total_size),
            'X-Upload-Content-Type': 'application/octet-stream'
        }

        # Step 1: Initiate the resumable upload
        endpoint = '/files#resumable'
        data = {
            'filename': filename,
        }
        response = self.api_client.post(endpoint, data=json.dumps(data), headers=headers)

        if response.status_code == 201:
            location_uri = response.headers['Location']
            self.logger.debug(f'Location URI: {location_uri}')
            upload_key = get_key_value_from_uri(location_uri)
            self.logger.info('Resumable upload initiated successfully')
            return location_uri, upload_key
        else:
            raise Exception(f'Failed to initiate resumable upload. Status code: {response.status_code}')

    def upload_chunk(self, upload_uri: str, total_size: int, chunk_data: bytes, chunk_start: int, chunk_end: int):
        """
        Upload a chunk of data.

        :param upload_uri: The upload URI (obtained from the response of the start_upload method)
        :param total_size: The total file size (in bytes)
        :param chunk_data: The chunk data (bytes)
        :param chunk_start: The start position of the chunk (0-based)
        :param chunk_end: The end position of the chunk (0-based)
        :return: Response headers (includes location) if the upload was successful, False otherwise
        """
        self.logger.info(f'Uploading chunk {chunk_start}-{chunk_end}/{total_size}')

        headers = {
            'Content-Range': f'bytes {chunk_start}-{chunk_end}/{total_size}',
            'Content-Type': 'application/octet-stream',
            'Content-Length': str(chunk_end - chunk_start + 1),
        }

        # Step 2: Upload the chunk
        response = self.api_client.put(upload_uri, data=chunk_data, headers=headers)

        self.logger.info(f'Response status code: {response.status_code}')

        self.logger.debug(f'Response headers: {response.headers}')
        self.logger.debug(f'Response text: {response.text}')

        if response.status_code == 201:
            # return True  # Chunk uploaded successfully
            return response.headers
        elif response.status_code == 308:
            return False  # Chunk upload is still in progress
        else:
            self.logger.error(response.text)
            raise Exception(f'Failed to upload chunk. Status code: {response.status_code}')

    def simulate_chunk_upload(self, buffer: bytes, chunk_size=5242880, filename=None):
        """
        Simulate chunk upload.

        :param buffer: The file buffer
        :param chunk_size: The chunk size in bytes (default: 5 MB)
        :param filename: The filename (default: random filename)
        :return: Response headers (includes location) if the upload was successful, False otherwise
        """
        try:
            # Seek to the end of the file
            buffer.seek(0, 2)  # 0 indicates the offset and 2 indicates seeking from the end of the file
            # Get the current file position, which is the length of the file
            total_size = buffer.tell()
            buffer.seek(0)  # Reset the file position to the beginning of the file

            self.logger.info(f'Total file size: {total_size}')

            if not filename:
                # Use a random filename
                filename = os.urandom(16).hex()

            upload_uri, upload_key = self.start_upload(filename, total_size)

            chunk_start = 0
            while chunk_start < (total_size - 1):
                chunk_end = min(chunk_start + chunk_size - 1, total_size - 1)
                chunk_data = buffer.read(chunk_end - chunk_start + 1)
                success = self.upload_chunk(upload_uri, total_size, chunk_data, chunk_start, chunk_end)

                chunk_start = chunk_end + 1

                if success:
                    # We are done here
                    self.logger.info('Response headers: ', success)
                    # break
                    pass

            self.logger.info('Resumable upload completed successfully')
            return success
        except Exception as e:
            self.logger.error(f'Error: {e}')
            # raise e
            return False
