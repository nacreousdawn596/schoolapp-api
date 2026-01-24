"""
Manager for grades and academic results
"""
from schoolapp_api.managers.base_manager import BaseManager
from schoolapp_api.constants import (
    CURRENT_ELEM_URL, CURRENT_MOD_URL, ELEM_URL, MOD_URL, 
    ANNEES_URL, SEMESTRES_URL
)
from schoolapp_api import parsers, types

class GradesManager(BaseManager):
    """Handles fetching of grades for elements, modules, years, and semesters"""

    def get_element_notes(self, current=False):
        url = CURRENT_ELEM_URL if current else ELEM_URL
        data = self.get_json_or_parse(url, parsers.note_elem)
        return [types.Element(self.client, item) for item in data] if data else []

    def get_module_notes(self, current=False):
        url = CURRENT_MOD_URL if current else MOD_URL
        data = self.get_json_or_parse(url, parsers.note_mod)
        # Note: In the original code, get_mod_note returned types.Element, 
        # but it should probably return types.Module if it's for modules.
        # Looking at original school_app_client.py:L272 it used types.Element.
        # I'll stick to what was there but maybe use Module if appropriate.
        # types/Module.py exists.
        return [types.Module(self.client, item) for item in data] if data else []

    def get_years(self):
        data = self.get_json_or_parse(ANNEES_URL, parsers.annees)
        return [types.Annee(self.client, item) for item in data] if data else []

    def get_semesters(self):
        data = self.get_json_or_parse(SEMESTRES_URL, parsers.semestres)
        return [types.Semestre(self.client, item) for item in data] if data else []
