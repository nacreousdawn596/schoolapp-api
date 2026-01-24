from bs4 import BeautifulSoup
import re

def parse(html_content):
    """Parse HTML content containing absence details."""
    soup = BeautifulSoup(html_content, 'html.parser')
    result = {"summary": [], "details": []}
    
    tables = soup.find_all('table', class_='table table-striped table-sm')
    if len(tables) < 2:
        return result
    
    # Summary
    for row in tables[0].find_all('tr')[1:]:
        cells = row.find_all('td')
        if len(cells) >= 4:
            result["summary"].append({
                "CodeElem": cells[0].get_text(strip=True),
                "Intitule": cells[1].get_text(strip=True),
                "Non_Justifiee": int(cells[2].get_text(strip=True) or 0),
                "Justifiee": int(cells[3].get_text(strip=True) or 0)
            })
            
    # Details
    for row in tables[1].find_all('tr')[1:]:
        cells = row.find_all('td')
        if len(cells) >= 5:
            result["details"].append({
                "Element": cells[0].get_text(strip=True),
                "Date": cells[1].get_text(strip=True),
                "Seance": cells[2].get_text(strip=True),
                "Justif": cells[3].get_text(strip=True).lower() == "true",
                "Remarques": cells[4].get_text(strip=True)
            })
            
    # Semester info
    alerts = soup.find_all('div', class_='alert alert-info')
    for alert in alerts:
        text = alert.get_text()
        if "semestre" in text.lower():
            match = re.search(r'S\d', text)
            if match:
                result["semestre"] = match.group()
    
    return result