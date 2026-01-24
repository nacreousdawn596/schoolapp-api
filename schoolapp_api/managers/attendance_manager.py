"""
Manager for attendance and sanctions
"""
from schoolapp_api.managers.base_manager import BaseManager
from schoolapp_api.constants import ABSENCES_URL, SANCTIONS_URL
from schoolapp_api import parsers

class AttendanceManager(BaseManager):
    """Handles fetching of absences and sanctions"""

    def get_absences(self):
        return self.get_json_or_parse(ABSENCES_URL, parsers.absences)

    def get_sanctions(self):
        return self.get_json_or_parse(SANCTIONS_URL, parsers.sanctions)
