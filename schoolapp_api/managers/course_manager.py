"""
Manager for courses and study plans
"""
import logging
from schoolapp_api.managers.base_manager import BaseManager
from schoolapp_api.constants import MODULES_URL
from schoolapp_api import parsers

logger = logging.getLogger(__name__)

class CourseManager(BaseManager):
    """Handles fetching of modules and study plans"""

    def get_modules(self, niveau, filiere, semestre, refresh_csrf=False):
        """Fetch modules for specific niveau/filiere/semestre"""
        if not self.ensure_logged_in():
            return None
        
        # Always GET modules page first to refresh CSRF token
        logger.info("Opening modules page to refresh state...")
        code, url, content = self.http_client.get(MODULES_URL)
        
        if not content:
            return None
        
        self.auth.update_csrf_token(content)
        
        if refresh_csrf:
            self.auth.refresh_csrf_from_url(MODULES_URL)
        
        logger.info(f"Fetching modules for {niveau} {filiere} {semestre}...")
        modules_data = {
            '_csrf': self.auth.csrf_token,
            'niveau': niveau,
            'filiere': filiere,
            'semestre': semestre
        }
        
        code, response_url, content = self.http_client.post(
            MODULES_URL,
            modules_data,
            referer=MODULES_URL
        )
        
        return parsers.modules.parse(content)
