# Up2Share API SDK for Python

[![PyPI version](https://badge.fury.io/py/u2s-sdk.svg)](https://badge.fury.io/py/u2s-sdk)
[![Build Status](https://travis-ci.com/up2share/u2s-sdk.svg?branch=master)](https://travis-ci.com/up2share/u2s-sdk)
[![codecov](https://codecov.io/gh/up2share/u2s-sdk/branch/master/graph/badge.svg)](https://codecov.io/gh/up2share/u2s-sdk)
[![Documentation Status](https://readthedocs.org/projects/u2s-sdk/badge/?version=latest)](https://u2s-sdk.readthedocs.io/en/latest/?badge=latest)

This README provides a step-by-step guide on how to use the `u2s-sdk` to perform a resumable file upload using Python. The `u2s-sdk` is a library that helps you easily upload large files to the [Up2Share](https://up2sha.re/) platform with resumable uploads.

## Prerequisites

Before you get started, ensure you have the following:

- Python (3.6 or later) installed on your system.
- Your Up2Share API key (or OAuth token), which you can obtain from your Up2Share account.

## Getting Started

1. Install the required dependencies:

   ```bash
   pip install u2s-sdk
   ```

2. Include the `u2s-sdk` in your project:

   ```python
   from u2s_sdk.handler import ResumableUploadHandler
   from u2s_sdk.client import ApiClient
   ```

3. Create an Up2Share `ApiClient` instance by providing your API key and the base URL:

   ```python
   api_key = 'your_api_key'
   api_client = ApiClient('https://api.up2sha.re', api_key=api_key, timeout=60)
   ```

4. Initialize the `ResumableUploadHandler` using the `ApiClient`:

   ```python
   handler = ResumableUploadHandler(api_client)
   ```

5. Specify the file you want to upload, the chunk size, and open the file:

   ```python
   file_name = 'your_file.mp4'
   file_path = 'path/to/your/file/your_file.mp4'
   chunk_size = 1048576  # 1 MB

   with open(file_path, 'rb') as file:
       handler.simulate_chunk_upload(file, chunk_size, filename=file_name)
   ```

6. Save and run your Python script.

## Uploading Large Files

With this setup, your Python script will upload the specified file to Up2Share using resumable uploads with the given chunk size. The `simulate_chunk_upload` method automatically takes care of splitting and uploading the file in chunks.

## Error Handling

If any issues occur during the upload process, the `ResumableUploadHandler` class handles exceptions and reports errors in the log.

## Development

### Run tests

First, make sure you have installed the required dependencies:

```bash
pip install -r requirements-dev.txt
```

Then, run the tests:

```bash
pytest
```

### Build Sphinx documentation

```bash
cd docs
make html
```

### Install package

```bash
pip install -e .
```
