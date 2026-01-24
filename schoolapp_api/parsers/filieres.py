from bs4 import BeautifulSoup

def parse(html_content):
    """
    Parse HTML content containing a table of academic programs and return structured data.
    
    Args:
        html_content (str): HTML content as a string
        
    Returns:
        list: List of dictionaries with program information
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the table - using multiple selectors to be safe
    table = soup.find('table', class_='table table-striped table-sm mb-1 display')
    
    if not table:
        # Try alternative selector
        table = soup.find('table', {'class': 'table'})
    
    if not table:
        return []
    
    # Extract table headers
    headers = []
    thead = table.find('thead')
    if thead:
        header_row = thead.find('tr')
        if header_row:
            for th in header_row.find_all('th'):
                headers.append(th.get_text(strip=True))
    
    # If headers weren't found in thead, use hardcoded ones
    if not headers:
        headers = ["Code", "Intitule", "Departement", "Accreditation", "Descriptif", "Plan_Etudes"]
    
    # Clean up header names (replace underscores with spaces, fix capitalization)
    cleaned_headers = []
    for header in headers:
        if header == "Plan_Etudes":
            cleaned_headers.append("Plan d'Etude")
        else:
            cleaned_headers.append(header)
    
    # Extract table rows
    data = []
    tbody = table.find('tbody')
    
    if not tbody:
        tbody = table  # If no tbody, search in table directly
    
    for row in tbody.find_all('tr'):
        cells = row.find_all('td')
        
        if len(cells) >= len(cleaned_headers):
            row_data = {}
            for i, cell in enumerate(cells[:len(cleaned_headers)]):
                cell_text = cell.get_text(strip=True)
                row_data[cleaned_headers[i]] = cell_text
            data.append(row_data)
    
    return data