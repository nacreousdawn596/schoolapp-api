from bs4 import BeautifulSoup

def parse(html_content):
    """Extract statistics from modal/popup HTML content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    stat_divs = soup.find_all('div', class_=lambda x: x and 'stat' in x.lower())
    
    expected_keys = ["Votre note", "Moyenne promo", "Max", "Min", "Ecart type", "Effectif", "Votre classement"]
    
    for div in stat_divs:
        for table in div.find_all('table'):
            rows = table.find_all('tr')
            if len(rows) < 7:
                continue
                
            stats = {}
            for row in rows:
                th, td = row.find('th'), row.find('td')
                if th and td:
                    key, val = th.get_text(strip=True), td.get_text(strip=True)
                    try:
                        if key in ["Effectif", "Votre classement"]:
                            stats[key.replace(" ", "_")] = int(float(val))
                        elif key in ["Votre note", "Moyenne promo", "Max", "Min", "Ecart type"]:
                            stats[key.replace(" ", "_")] = float(val)
                        else:
                            stats[key.replace(" ", "_")] = val
                    except (ValueError, TypeError):
                        stats[key.replace(" ", "_")] = val
            
            if all(k in stats for k in expected_keys):
                return stats
                
    return {}