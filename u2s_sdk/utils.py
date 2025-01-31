"""
u2s_sdk.utils
"""
from urllib.parse import urlparse, parse_qs


def get_key_value_from_uri(uri: str):
    """
    Get the key value from a URI.
    :param uri: The URI
    :return: The upload key value
    """
    # Parse the URI
    parsed_uri = urlparse(uri)

    # Get the query parameters as a dictionary
    query_parameters = parse_qs(parsed_uri.query)

    # Retrieve the value of the "key" parameter
    key_value = query_parameters.get("key", [None])[0]

    return key_value
