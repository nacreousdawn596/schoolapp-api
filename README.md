# School App Client - Refactored

Clean, organized structure for the School App client with proper separation of concerns.

## 📁 Project Structure

```
├── http_client.py         # Base HTTP client (GET/POST requests, cookie management)
├── auth.py                # Authentication & CSRF token handling
├── school_app_client.py   # Main API client (combines everything)
└── example_usage.py       # Usage example
```

## 🎯 Architecture

### 1. **http_client.py** - HTTP Layer
- Handles raw HTTP operations (GET/POST)
- Cookie jar and session management
- Common headers configuration
- Error handling for network requests

### 2. **auth.py** - Authentication Layer
- Login flow management
- CSRF token extraction and updates
- Session state tracking
- Decoupled from HTTP implementation

### 3. **school_app_client.py** - API Layer
- High-level API methods (`get_filieres()`, `get_modules()`)
- Orchestrates HTTP client and auth manager
- Business logic for School App endpoints

## 🚀 Usage

```python
from school_app_client import SchoolAppClient

# Initialize
client = SchoolAppClient()

# Login
client.login("your.email@example.com", "password")

# Fetch data
filieres = client.get_filieres()
modules = client.get_modules(niveau="1A", filiere="API-MPT", semestre="S1")

# If you encounter 403 errors, force CSRF refresh
modules = client.get_modules(
    niveau="1A", 
    filiere="API-MPT", 
    semestre="S1",
    refresh_csrf=True
)
```

## ✨ Benefits of This Structure

- **Separation of Concerns**: Each module has a single responsibility
- **Testability**: Easy to mock and unit test each layer
- **Maintainability**: Changes in one layer don't affect others
- **Extensibility**: Easy to add new endpoints or authentication methods
- **Reusability**: HTTP client can be used for other projects

## 🎯 Key Features

- **Automatic CSRF Management**: CSRF tokens are automatically refreshed from page content
- **Session Persistence**: Cookie-based session management keeps you logged in
- **Smart Error Handling**: Detects 403 errors and suggests CSRF refresh
- **Optional CSRF Force Refresh**: Use `refresh_csrf=True` to force token refresh before requests
- **Clean Separation**: HTTP, Auth, and API layers are completely decoupled

## 🔧 Potential Extensions

- Add logging module
- Implement response parsers (HTML → structured data)
- Add caching layer
- Create async version using `aiohttp`
- Add retry logic with exponential backoff
