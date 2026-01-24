from bs4 import BeautifulSoup

def parse(html_content):
    """Parse HTML content containing semester averages."""
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', class_='table table-striped table-sm') or soup.find('table')
    
    if not table:
        return []
    
    headers = [th.get_text(strip=True) for th in table.find_all('th')]
    if len(headers) < 10:
        headers = ["Niveau", "Filiere", "Semestre", "AU", "Statut", "Moy SEM", "PJ", "Decision", "Classement", "Releve de Notes"]
    
    data = []
    tbody = table.find('tbody') or table
    
    for row in tbody.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) >= 10:
            row_data = {}
            for i, cell in enumerate(cells[:10]):
                if i == 9: # Download link
                    link = cell.find('a')
                    row_data[headers[i]] = link.get('href') if link else cell.get_text(strip=True)
                else:
                    val = cell.get_text(strip=True)
                    if headers[i] in ["Moy SEM", "PJ"]:
                        try:
                            row_data[headers[i]] = float(val) if val and val != "--" else None
                        except ValueError:
                            row_data[headers[i]] = val
                    else:
                        row_data[headers[i]] = val
            data.append(row_data)
            
    return data