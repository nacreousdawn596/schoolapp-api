from .base import BaseType
from ..constants import EVAL_STAT_URL

class Element(BaseType):
    """Represents a module element (subject) with grades"""
    
    def fetch_stats(self, eval_type):
        """Generic stat fetcher for element evaluations"""
        note_map = {
            "NoteCC": getattr(self, "CC", None),
            "NoteEX": getattr(self, "EX", None),
            "NoteTP": getattr(self, "TP", None),
            "NoteRAT": getattr(self, "RAT", None),
            "MoyElem": getattr(self, "Moy", None)
        }
        
        params = {
            'eval': eval_type,
            'codeelem': self.CodeElem,
            'note': note_map.get(eval_type),
            'au': self.AU
        }
        
        stats = self._get_stats(EVAL_STAT_URL, params)
        if stats:
            self._stats[eval_type] = stats
        return stats

    @property
    def cc_stats(self):
        return self._stats.get("NoteCC") or self.fetch_stats("NoteCC")
    
    @property
    def ex_stats(self):
        return self._stats.get("NoteEX") or self.fetch_stats("NoteEX")
    
    @property
    def tp_stats(self):
        return self._stats.get("NoteTP") or self.fetch_stats("NoteTP")
    
    @property
    def moy_stats(self):
        return self._stats.get("MoyElem") or self.fetch_stats("MoyElem")
    
    @property
    def rat_stats(self):
        return self._stats.get("NoteRAT") or self.fetch_stats("NoteRAT")
