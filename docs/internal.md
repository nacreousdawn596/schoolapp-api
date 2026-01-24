# Internal Utilities

This page documents the internal components that handle networking, authentication, and constants.

## `HTTPClient`

A wrapper around `urllib` that handles session management and cookies.

### Methods
- **`__init__(self, base_url)`**: Initializes the client with a cookie jar and default headers.
- **`get(self, url, params=None)`**: Performs a GET request.
    - `url`: The target URL.
    - `params`: Optional dictionary of query parameters.
    - Returns: `(status_code, response_url, content)`.
- **`post(self, url, data, referer=None)`**: Performs a POST request.
    - `url`: The target URL.
    - `data`: Dictionary of form data.
    - `referer`: Optional referer header value.
    - Returns: `(status_code, response_url, content)`.

---

## `AuthManager`

Handles authentication and CSRF token extraction.

### Attributes
- **`csrf_token`**: The current CSRF token retrieved from the application.
- **`logged_in`**: Boolean indicating the current login status.

### Methods
- **`extract_csrf_token(html_content)`** (Static): Extracts the `_csrf` value from HTML using regex.
- **`update_csrf_token(self, html_content)`**: Updates the internal `csrf_token` from provided HTML content.
- **`login(self, email, password)`**: Performs the login flow (GET login page, extract CSRF, POST credentials).
- **`is_logged_in(self)`**: Returns whether the manager is currently logged in.
- **`refresh_csrf_from_url(self, url)`**: Fetches a specific URL to refresh the CSRF token.

---

## `Constants`

Centralized location for URLs and default headers used by the library.

### Key Constants
- **`BASE_URL`**: `https://schoolapp.ensam-umi.ac.ma`
- **`LOGIN_URL`**: Endpoint for authentication.
- **`INDEX_URL`**: Student profile endpoint.
- **`DEFAULT_HEADERS`**: Browser-like headers to ensure compatibility.
- Various URLs for grades, attendance, and statistics.
