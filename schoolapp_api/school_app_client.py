"""
Professional client for interacting with the School App
"""
from schoolapp_api.http_client import HTTPClient
from schoolapp_api.auth import AuthManager
from schoolapp_api.constants import BASE_URL
from schoolapp_api.managers import (
    GradesManager, AttendanceManager, ProfileManager, CourseManager
)

class SchoolAppClient:
    """Main client for the School App API"""
    
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
        self.http_client = HTTPClient(self.base_url)
        self.auth = AuthManager(self.http_client, self.base_url)
        
        # Initialize Managers
        self.grades = GradesManager(self)
        self.attendance = AttendanceManager(self)
        self.profile = ProfileManager(self)
        self.courses = CourseManager(self)
        
    def login(self, email, password):
        """Authenticate user"""
        return self.auth.login(email, password)
    
    # ---------------------------------------------------------
    # Legacy / Convenience methods for backward compatibility
    # ---------------------------------------------------------
    
    def get_profile(self):
        return self.profile.get_profile()
    
    def get_filieres(self):
        return self.profile.get_filieres()
    
    def get_absences(self):
        return self.attendance.get_absences()
    
    def get_sanctions(self):
        return self.attendance.get_sanctions()
    
    def get_elem_note(self):
        return self.grades.get_element_notes()
    
    def get_current_elem_note(self):
        return self.grades.get_element_notes(current=True)
    
    def get_mod_note(self):
        return self.grades.get_module_notes()
    
    def get_current_mod_note(self):
        return self.grades.get_module_notes(current=True)
    
    def get_annee(self):
        return self.grades.get_years()
    
    def get_semestre(self):
        return self.grades.get_semesters()
    
    def get_modules(self, niveau, filiere, semestre, refresh_csrf=False):
        return self.courses.get_modules(niveau, filiere, semestre, refresh_csrf)