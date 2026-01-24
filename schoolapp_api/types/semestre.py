from .base import BaseType
from ..constants import SEM_STAT_URL

class Semestre(BaseType):
    """Represents a semester result"""
    
    def fetch_stats(self):
        params = {
            'eval': "MoySem",
            'niveau': getattr(self, "Niveau", None),
            'filiere': getattr(self, "Filiere", None),
            'semestre': getattr(self, "Semestre", None),
            'au': getattr(self, "AU", None),
            'note': getattr(self, "Moy_SEM", None)
        }
        
        stats = self._get_stats(SEM_STAT_URL, params)
        if stats:
            self._stats["MoySem"] = stats
        return stats
        
    @property
    def stats(self):
        return self._stats.get("MoySem") or self.fetch_stats()