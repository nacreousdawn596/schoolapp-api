"""
Centralized constants for the School App API
"""

BASE_URL = "https://schoolapp.ensam-umi.ac.ma"

# Endpoints
LOGIN_URL = f"{BASE_URL}/login"
INDEX_URL = f"{BASE_URL}/index"
MODULES_URL = f"{BASE_URL}/plan-etudes-view/modules"
FILIERES_URL = f"{BASE_URL}/plan-etudes-view/filieres"

# Student Grade Endpoints
CURRENT_ELEM_URL = f"{BASE_URL}/student/noteselem-encours"
CURRENT_MOD_URL = f"{BASE_URL}/student/notesmod-encours"
ELEM_URL = f"{BASE_URL}/student/noteselem"
MOD_URL = f"{BASE_URL}/student/notesmod"
ANNEES_URL = f"{BASE_URL}/student/notesannee"
SEMESTRES_URL = f"{BASE_URL}/student/notessem"

# Absence and Sanctions Endpoints
ABSENCES_URL = f"{BASE_URL}/student/absence/bilan"
SANCTIONS_URL = f"{BASE_URL}/student/absence/sanctions"

# Stats Endpoints
EVAL_STAT_URL = f"{BASE_URL}/notes-stat/elemevalsat"
MOD_STAT_URL = f"{BASE_URL}/notes-stat/modsat"
ANNEE_STAT_URL = f"{BASE_URL}/notes-stat/anneesat"
SEM_STAT_URL = f"{BASE_URL}/notes-stat/semsat"

# Default Headers
DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}
