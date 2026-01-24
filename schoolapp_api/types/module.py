from .base import BaseType
from ..constants import MOD_STAT_URL

class Module(BaseType):
    """Represents a module (collection of elements) with grades"""
    
    def fetch_stats(self):
        params = {
            'eval': "MOYMOD",
            'codemod': getattr(self, "CodeMod", None),
            'note': getattr(self, "Moy", None),
            'au': getattr(self, "AU", None)
        }
        
        stats = self._get_stats(MOD_STAT_URL, params)
        if stats:
            self._stats["MOYMOD"] = stats
        return stats

    @property
    def stats(self):
        return self._stats.get("MOYMOD") or self.fetch_stats()