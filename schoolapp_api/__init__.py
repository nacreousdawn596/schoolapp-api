"""
Professional School App API Client
"""

from .school_app_client import SchoolAppClient
from .http_client import HTTPClient
from .auth import AuthManager

__version__ = "2.0.0"
__all__ = ["SchoolAppClient", "HTTPClient", "AuthManager"]
