"""
Client module.

u2s_sdk.client
"""
import logging
import requests


class ApiClient:
    """
    API client.
    """
    def __init__(self, base_url='https://api.up2sha.re', timeout=10, api_key=None, oauth_token=None):
        """
        Constructor.

        :param base_url: The base URL (default: https://api.up2sha.re)
        :param timeout: The timeout (in seconds)
        :param api_key: The API key (optional)
        :param oauth_token: The OAuth token (optional)
        """
        self.base_url = base_url
        self.timeout = timeout
        self.api_key = api_key
        self.oauth_token = oauth_token

        # default logging level and format
        self.set_logging()

    # a method that defines the request logging level and format
    def set_logging(self, level: int =logging.DEBUG, fmt: str ='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
        """
        Set logging.

        :param level: The logging level (default: logging.DEBUG)
        :param fmt: The logging format (default: '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        """
        logger = logging.getLogger(__name__)
        logger.setLevel(level)
        # Create a console handler
        console_handler = logging.StreamHandler()
        # Set the formatter for the console handler (customize this as needed)
        formatter = logging.Formatter(fmt)
        console_handler.setFormatter(formatter)
        # Add the console handler to the logger
        logger.addHandler(console_handler)

        # Store the logger in the class
        self.logger = logger
        self._set_requests_logging(level, fmt)

    # method to get the logger
    def get_logger(self):
        """
        Get the logger.

        :return: The logger
        """
        return self.logger

    # same for the request library
    def _set_requests_logging(self, level: int, fmt: str):
        """
        Set logging for the requests library.

        :meta private:

        :param level: The logging level
        :param fmt: The logging format
        """
        logging.getLogger("requests").setLevel(level)
        logging.getLogger("urllib3").setLevel(level)
        # Create a console handler
        console_handler = logging.StreamHandler()
        # Set the formatter for the console handler (customize this as needed)
        formatter = logging.Formatter(fmt)
        console_handler.setFormatter(formatter)
        # Add the console handler to the logger
        logging.getLogger("requests").addHandler(console_handler)
        logging.getLogger("urllib3").addHandler(console_handler)

        # from http.client import HTTPConnection  # py3

        # # print statements from `http.client.HTTPConnection` to console/stdout
        # HTTPConnection.debuglevel = 1

    def get_headers(self):
        """
        Get the headers.

        :return: The headers
        """
        headers = {
            # 'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        if self.api_key:
            headers['X-Api-Key'] = self.api_key

        if self.oauth_token:
            headers['Authorization'] = f'Bearer {self.oauth_token}'

        return headers

    def get(self, endpoint: str, headers=None):
        """
        Perform a GET request.

        :param endpoint: The endpoint
        :param headers: The headers
        :return: The response
        """
        return self._make_request('GET', endpoint, headers=headers)

    def post(self, endpoint:str , data=None, headers=None):
        """
        Perform a POST request.

        :param endpoint: The endpoint
        :param data: The data
        :param headers: The headers
        :return: The response
        """
        return self._make_request('POST', endpoint, data=data, headers=headers)

    def put(self, endpoint: str, data=None, headers=None):
        """
        Perform a PUT request.

        :param endpoint: The endpoint
        :param data: The data
        :param headers: The headers
        :return: The response
        """
        return self._make_request('PUT', endpoint, data=data, headers=headers)

    def delete(self, endpoint: str, headers=None):
        """
        Perform a DELETE request.

        :param endpoint: The endpoint
        :param headers: The headers
        :return: The response
        """
        return self._make_request('DELETE', endpoint, headers=headers)

    def _make_request(self, method: str, endpoint: str, data=None, headers=None):
        """
        Make a request.

        :param method: The method
        :param endpoint: The endpoint
        :param data: The data
        :param headers: The headers
        :return: The response
        """
        url = f'{self.base_url}/{endpoint}'
        _headers = self.get_headers()

        # Merge the headers
        if headers:
            _headers.update(headers)
        headers = _headers

        response = None

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, timeout=self.timeout)
            elif method == 'POST':
                response = requests.post(url, headers=headers, data=data, timeout=self.timeout)
            elif method == 'PUT':
                response = requests.put(url, headers=headers, data=data, timeout=self.timeout)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers, timeout=self.timeout)

            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            # print(f'Error: {e}')
            self.logger.error(f'Error: {e}')
            return None

        # return response.json()
        return response
