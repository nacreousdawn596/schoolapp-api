"""
Base client for shared manager logic
"""
import logging

logger = logging.getLogger(__name__)

class BaseManager:
    """Base class for all managers"""
    
    def __init__(self, client):
        self.client = client
        self.http_client = client.http_client
        self.auth = client.auth

    def ensure_logged_in(self):
        """Ensures the client is logged in before making requests"""
        if not self.auth.is_logged_in():
            logger.error("Not logged in! Call login() first.")
            return False
        return True

    def get_json_or_parse(self, url, parser, params=None, refresh_csrf=True):
        """Helper to fetch content, update CSRF, and parse"""
        if not self.ensure_logged_in():
            return None
            
        code, url, content = self.http_client.get(url, params=params)
        
        if not content:
            return None
            
        if refresh_csrf:
            self.auth.update_csrf_token(content)
            
        return parser.parse(content)
