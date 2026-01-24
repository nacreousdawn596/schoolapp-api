"""
Base class for domain models
"""
import logging

logger = logging.getLogger(__name__)

class BaseType:
    """Base class for all domain models with client access"""
    
    def __init__(self, client, data):
        self.client = client
        for key, value in data.items():
            # Clean up keys for valid python attributes
            clean_key = key.replace(" ", "_").replace("é", 'e').replace("è", 'e')
            setattr(self, clean_key, value)
        self._stats = {}

    def _ensure_logged_in(self):
        if not self.client.auth.is_logged_in():
            logger.error("Not logged in! Call login() first.")
            return False
        return True

    def _get_stats(self, url, params):
        if not self._ensure_logged_in():
            return None
        
        # Add CSRF token to params
        params['_csrf'] = self.client.auth.csrf_token
        
        code, url, content = self.client.http_client.get(url, params=params)
        from schoolapp_api.parsers.stats import parse
        return parse(content)
