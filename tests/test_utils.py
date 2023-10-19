from u2s_sdk.utils import get_key_value_from_uri

def test_get_key_value_from_uri_with_valid_key():
    uri = "https://example.com/path?key=value"
    result = get_key_value_from_uri(uri)
    assert result == "value"

def test_get_key_value_from_uri_with_missing_key():
    uri = "https://example.com/path?other=value"
    result = get_key_value_from_uri(uri)
    assert result is None

# def test_get_key_value_from_uri_with_multiple_keys():
#     uri = "https://example.com/path?key=value1&key=value2"
#     result = get_key_value_from_uri(uri)
#     assert result == "value1"

def test_get_key_value_from_uri_with_empty_uri():
    uri = ""
    result = get_key_value_from_uri(uri)
    assert result is None
