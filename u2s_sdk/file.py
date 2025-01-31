"""
File module.

u2s_sdk.file
"""
from .client import ApiClient


class FileHandler:
    """
    File handler.
    """
    def __init__(self, api_client: ApiClient):
        """
        Constructor.

        :param api_client: The API client
        """
        self.api_client = api_client
        self.logger = api_client.get_logger()
        self.limit = 100
        self.include = 'owner'
        self.search_join = 'and'

    def create_download_token(self, file_id: int):
        """
        Create a download token for a file.

        :param file_id: The file ID
        :return: The download token
        """
        endpoint = f'/files/{str(file_id)}/downloadtoken'
        response = self.api_client.get(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            # Handle error response here
            return None

    def get_raw(self, file_id: int, range_header: str, token: str, dl_token: str, dl_expiry: int|str):
        """
        Get the raw file data.

        :param file_id: The file ID
        :param range_header: The range header
        :param token: The token
        :param dl_token: The download token
        :param dl_expiry: The download expiry
        :return: The raw file data
        """
        endpoint = f'/files/{str(file_id)}/raw'
        headers = {
            'Range': range_header,
        }
        params = {
            'token': token,
            'dl-token': dl_token,
            'dl-expiry': dl_expiry,
        }
        response = self.api_client.get(endpoint, headers=headers, params=params)
        if response.status_code == 200:
            return response.content
        elif response.status_code == 206:
            # Handle partial content response here
            return response.content
        else:
            # Handle error response here
            return None

    def list(self, include=None, search=None, limit=None, search_join=None):
        """
        List files.

        :param include: The include parameter (owner|uploadKey|shares|activity)
        :param search: The search parameter
        :param limit: The limit parameter
        :param search_join: The search join parameter (or|and)
        :return: The file list
        """

        # Validate include parameter
        if include is not None:
            if include not in ['owner', 'uploadKey', 'shares', 'activity']:
                raise Exception('Invalid include parameter')
        else:
            include = self.include

        # Validate search_join parameter
        if search_join is not None:
            if search_join not in ['or', 'and']:
                raise Exception('Invalid search_join parameter')
        else:
            search_join = self.search_join

        # Validate limit parameter
        if limit is not None:
            if limit < 1 or limit > 100:
                raise Exception('Invalid limit parameter')
        else:
            limit = self.limit

        endpoint = '/files'
        params = {
            'include': include,
            'search': search,
            'limit': limit,
            'searchJoin': search_join,
        }
        response = self.api_client.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            # Handle error response here
            return None

    def delete(self, file_id: int):
        """
        Delete a file.

        :param file_id: The file ID
        :return: True if the deletion was successful, False otherwise
        """
        endpoint = f'/files/{str(file_id)}'
        response = self.api_client.delete(endpoint)
        if response.status_code == 204:
            # Deletion successful
            return True
        else:
            # Handle error response here
            return False

    def update(self, file_id: int, filename=None, description=None, visibility=None):
        """
        Update a file.

        :param file_id: The file ID
        :param filename: The filename
        :param description: The description
        :param visibility: The visibility
        :return: The updated file
        """
        endpoint = f'/files/{str(file_id)}'
        data = {
            'filename': filename,
            'description': description,
            'visibility': visibility,
        }
        response = self.api_client.put(endpoint, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            # Handle error response here
            return None
