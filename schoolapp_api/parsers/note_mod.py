from bs4 import BeautifulSoup

def parse(html_content):
    """Parse HTML content containing module grades."""
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', class_='table table-striped table-sm') or soup.find('table')
    
    if not table:
        return []
    
    headers = [th.get_text(strip=True) for th in table.find_all('th')]
    if len(headers) < 4:
        headers = ["CodeMod", "AU", "Moy", "Dec"]
    
    data = []
    tbody = table.find('tbody') or table
    
    for row in tbody.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) >= 4:
            row_data = {}
            for i, cell in enumerate(cells[:4]):
                val = cell.get_text(strip=True)
                if headers[i] == "Moy":
                    try:
                        row_data[headers[i]] = float(val) if val and val != "--" else None
                    except ValueError:
                        row_data[headers[i]] = val
                else:
                    row_data[headers[i]] = val
            data.append(row_data)
            
    return data