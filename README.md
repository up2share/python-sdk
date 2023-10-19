# Up2Share API SDK for Python

[![PyPI version](https://badge.fury.io/py/u2s-sdk.svg)](https://badge.fury.io/py/u2s-sdk)
[![Build Status](https://travis-ci.com/up2share/u2s-sdk.svg?branch=master)](https://travis-ci.com/up2share/u2s-sdk)
[![codecov](https://codecov.io/gh/up2share/u2s-sdk/branch/master/graph/badge.svg)](https://codecov.io/gh/up2share/u2s-sdk)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4b6b5b9b0b9a4b6e9b8b2b8b2b8b2b8b)](https://www.codacy.com/app/up2share/u2s-sdk?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=up2share/u2s-sdk&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/4b6b5b9b0b9a4b6e9b8b2b8b2b8b2b8b)](https://www.codacy.com/app/up2share/u2s-sdk?utm_source=github.com&utm_medium=referral&utm_content=up2share/u2s-sdk&utm_campaign=Badge_Coverage)
[![Documentation Status](https://readthedocs.org/projects/u2s-sdk/badge/?version=latest)](https://u2s-sdk.readthedocs.io/en/latest/?badge=latest)

This README provides a step-by-step guide on how to use the `u2s-sdk` to perform a resumable file upload using Python. The `u2s-sdk` is a library that helps you easily upload large files to the [Up2Share](https://up2sha.re/) platform with resumable uploads.

## Prerequisites

Before you get started, ensure you have the following:

- Python (3.6 or later) installed on your system.
- Your Up2Share API key (or OAuth token), which you can obtain from your Up2Share account.

## Getting Started

1. Clone or download the `u2s-sdk` library from the [GitHub repository](https://github.com/up2share/u2s-sdk).

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Include the `u2s-sdk` in your project:

   ```python
   from u2s_sdk.handler import ResumableUploadHandler
   from u2s_sdk.client import ApiClient
   ```

4. Create an Up2Share `ApiClient` instance by providing your API key and the base URL:

   ```python
   api_key = 'your_api_key'
   api_client = ApiClient('https://api.up2sha.re', api_key=api_key, timeout=60)
   ```

5. Initialize the `ResumableUploadHandler` using the `ApiClient`:

   ```python
   handler = ResumableUploadHandler(api_client)
   ```

6. Specify the file you want to upload, the chunk size, and open the file:

   ```python
   file_name = 'your_file.mp4'
   file_path = 'path/to/your/file/your_file.mp4'
   chunk_size = 1048576  # 1 MB

   with open(file_path, 'rb') as file:
       handler.simulate_chunk_upload(file, chunk_size, filename=file_name)
   ```

7. Save and run your Python script.

## Uploading Large Files

With this setup, your Python script will upload the specified file to Up2Share using resumable uploads with the given chunk size. The `simulate_chunk_upload` method automatically takes care of splitting and uploading the file in chunks.

## Error Handling

If any issues occur during the upload process, the `ResumableUploadHandler` class handles exceptions and reports errors in the log.

## Development

### Install package

```bash
pip install -e .
```
