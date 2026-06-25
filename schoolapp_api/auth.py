"""
Authentication and CSRF token management
"""
import re
import logging
from schoolapp_api.constants import LOGIN_URL

logger = logging.getLogger(__name__)

class AuthManager:
    """Handles authentication and CSRF token management"""
    
    def __init__(self, http_client, base_url):
        self.http_client = http_client
        self.base_url = base_url
        self.login_url = LOGIN_URL
        self.csrf_token = None
        self.logged_in = False
    
    @staticmethod
    def extract_csrf_token(html_content):
        """Extract CSRF token from HTML content"""
        match = re.search(r'name=["\']_csrf["\']\s+value=["\']([^"\']+)["\']', html_content)
        return match.group(1) if match else None
    
    def update_csrf_token(self, html_content):
        """Update CSRF token from HTML content"""
        new_csrf = self.extract_csrf_token(html_content)
        if new_csrf:
            self.csrf_token = new_csrf
            return True
        return False
    
    def login(self, email, password):
        """Login and maintain session"""
        if self.logged_in:
            logger.info("Already logged in!")
            return True
        
        logger.info("Fetching login page...")
        code, url, content = self.http_client.get(self.login_url)
        
        if not content or not self.update_csrf_token(content):
            logger.error("Failed to fetch login page or retrieve CSRF token.")
            return False
        
        logger.info(f"Got CSRF token, logging in...")
        login_data = {
            '_csrf': self.csrf_token,
            'email': email,
            'password': password
        }
        
        code, response_url, content = self.http_client.post(
            self.login_url, 
            login_data, 
            referer=self.login_url
        )
        
        if response_url and ("/login" in response_url and "error" in response_url):
            logger.error("Login failed! Invalid credentials.")
            return False
        
        logger.info("Login successful!")
        self.logged_in = True
        return True
    
    def is_logged_in(self):
        """Check if currently logged in"""
        return self.logged_in
    
    def check_session(self):
        """Confirm whether the session is still valid by visiting the index page"""
        try:
            from schoolapp_api.constants import INDEX_URL
            code, url, content = self.http_client.get(INDEX_URL)

            # If url is None (exception) or it contains "/login", session is dead
            if not url or "/login" in url.lower():
                logger.warning(f"Session check: Redirected to {url or 'None'} - session invalid")
                self.logged_in = False
                return False
            
            # If content is very short or contains login-like keywords, it's also dead
            if content and (len(content) < 1000 or "login" in content.lower()[:500]):
                logger.warning("Session check: Content looks like a login page - session invalid")
                self.logged_in = False
                return False

            self.logged_in = True
            return True
        except Exception as e:
            logger.error(f"Error during check_session: {e}")
            self.logged_in = False
            return False

    def refresh_csrf_from_url(self, url):
        """Fetch a fresh CSRF token from a specific page"""
        try:
            code, response_url, content = self.http_client.get(url)
            if content and self.update_csrf_token(content):
                return True
            return False
        except Exception as e:
            logger.warning(f"CSRF refresh warning: {e}")
            return False
