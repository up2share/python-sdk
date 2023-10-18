import os

from u2s_sdk.handler import ResumableUploadHandler
from u2s_sdk.client import ApiClient


def main():
    api_client = ApiClient('https://api.up2sha.re', api_key='your_api_key', timeout=30)

    # Initialize the ResumableUploadHandler
    handler = ResumableUploadHandler(api_client)

    # Example usage for resumable upload with specified chunk size
    file_name = 'file_example_MP4_1920_18MG.mp4'
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    chunk_size = 1048576  # 1 MB

    with open(file_path, 'rb') as file:
        handler.simulate_chunk_upload(file, chunk_size, filename=file_name)


if __name__ == "__main__":
    main()
