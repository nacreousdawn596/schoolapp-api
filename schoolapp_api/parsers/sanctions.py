from bs4 import BeautifulSoup
import re

def parse(html_content):
    """Parse HTML content containing disciplinary sanctions."""
    soup = BeautifulSoup(html_content, 'html.parser')
    result = {
        "Absences_non_justifiees": 0,
        "Absences_justifiees": 0,
        "Sanction": "",
        "Message": "",
        "Elements_non_autorises": []
    }
    
    table = soup.find('table', class_='table table-striped table-sm') or soup.find('table')
    if table:
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) == 2:
                key = cells[0].get_text(strip=True)
                val_cell = cells[1]
                val_text = val_cell.get_text(strip=True)
                
                if "non justifiées" in key:
                    result["Absences_non_justifiees"] = int(val_text or 0)
                elif "justifiées" in key:
                    result["Absences_justifiees"] = int(val_text or 0)
                elif key == "Sanction":
                    btn = val_cell.find('button')
                    result["Sanction"] = btn.get_text(strip=True) if btn else val_text
                elif key == "Message":
                    result["Message"] = val_text
                elif "pas autorisé" in key:
                    result["Elements_non_autorises"] = [b.get_text(strip=True) for b in val_cell.find_all('button', class_='elem')]

    alert = soup.find('div', class_='alert alert-info')
    if alert:
        match = re.search(r'S\d', alert.get_text())
        if match:
            result["Semestre"] = match.group()
            
    return result