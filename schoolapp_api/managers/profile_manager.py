"""
Manager for student profile and programs
"""
from schoolapp_api.managers.base_manager import BaseManager
from schoolapp_api.constants import INDEX_URL, FILIERES_URL
from schoolapp_api import parsers

class ProfileManager(BaseManager):
    """Handles fetching of student profile and filieres"""

    def get_profile(self):
        return self.get_json_or_parse(INDEX_URL, parsers.profile)

    def get_filieres(self):
        return self.get_json_or_parse(FILIERES_URL, parsers.filieres)
