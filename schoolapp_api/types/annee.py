from .base import BaseType
from ..constants import ANNEE_STAT_URL

class Annee(BaseType):
    """Represents an academic year result"""
    
    def fetch_stats(self):
        params = {
            'eval': "MoyAn",
            'niveau': getattr(self, "Niveau", None),
            'filiere': getattr(self, "Filiere", None),
            'au': getattr(self, "AU", None),
            'note': getattr(self, "Moy_Annee", None)
        }
        
        stats = self._get_stats(ANNEE_STAT_URL, params)
        if stats:
            self._stats["MoyAn"] = stats
        return stats
        
    @property
    def stats(self):
        return self._stats.get("MoyAn") or self.fetch_stats()