# Python Network #1

This project focuses on working with HTTP requests in Python using both the `urllib` and `requests` packages. It includes scripts that demonstrate making HTTP requests, handling responses, working with APIs, and managing errors.

## Project Overview

The scripts in this repository demonstrate:
- Making HTTP GET and POST requests
- Handling response headers and body content
- Working with JSON data
- Error handling for HTTP requests
- Basic authentication with APIs
- GitHub API interaction

## Requirements
- Python 3.8.5
- Ubuntu 20.04 LTS
- pycodestyle 2.8.*
- requests library

## Files Description

* `0-hbtn_status.py`: Fetches a URL using urllib
* `1-hbtn_header.py`: Displays value of X-Request-Id header from a URL response
* `2-post_email.py`: Sends POST request with email parameter using urllib
* `3-error_code.py`: Handles HTTP errors with urllib
* `4-hbtn_status.py`: Fetches a URL using requests
* `5-hbtn_header.py`: Displays X-Request-Id using requests
* `6-post_email.py`: Sends POST request with email using requests
* `7-error_code.py`: Handles HTTP errors with requests
* `8-json_api.py`: Sends POST request with letter parameter and handles JSON response
* `10-my_github.py`: Uses GitHub API with Basic Authentication
* `100-github_commits.py`: Lists recent commits of a GitHub repository

## Usage

```bash
# Example usage
./0-hbtn_status.py
./1-hbtn_header.py <URL>
./2-post_email.py <URL> <email>
```

Each script is executable and includes usage instructions in its documentation.
