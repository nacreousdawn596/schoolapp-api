from bs4 import BeautifulSoup
import re

def parse(html_content):
    """
    Parse HTML content containing user profile and return detailed user data.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    result = {
        "basic_info": {},
        "academic_info": {},
        "administrative_info": {},
        "personal_info": {},
        "family_info": {},
        "contact_info": {},
        "download_links": {},
        "sections": {}
    }
    
    # Extract from sidebar
    user_panel = soup.find('div', class_='user-panel')
    if user_panel:
        img = user_panel.find('img', class_='img-circle')
        if img and img.get('src'):
            result["basic_info"]["photo_url"] = img.get('src')
        
        info_div = user_panel.find('div', class_='info')
        if info_div:
            spans = info_div.find_all('span', class_='d-block')
            if len(spans) >= 2:
                result["basic_info"]["full_name"] = spans[0].get_text(strip=True)
                result["basic_info"]["role"] = spans[1].get_text(strip=True)
    
    # Extract welcome message
    alert_div = soup.find('div', class_='alert alert-info')
    if alert_div:
        result["basic_info"]["welcome_message"] = alert_div.get_text(strip=True)
    
    # Find all tables
    tables = soup.find_all('table', class_='table table-striped table-sm')
    
    if len(tables) >= 2:
        # Administrative data table
        for row in tables[0].find_all('tr'):
            cells = row.find_all(['th', 'td'])
            if len(cells) >= 2:
                key = cells[0].get_text(strip=True).rstrip(':').strip()
                val = cells[1].get_text(strip=True)
                result["administrative_info"][key] = val
        
        # Personal data table
        for row in tables[1].find_all('tr'):
            cells = row.find_all(['th', 'td'])
            if len(cells) >= 2:
                key = cells[0].get_text(strip=True).rstrip(':').strip()
                val = cells[1].get_text(strip=True)
                
                if key in ["Code", "CNE/Masar", "Nom", "Prénom", "Nom Arabe", "Prénom Arabe", "CIN", "Sexe", "Date Naissance", "Nationalité", "Lieu_Naissance"]:
                    result["personal_info"][key] = val
                elif key in ["Email", "Téléphone", "Adr_Parents", "Ville", "Tel_Parents"]:
                    result["contact_info"][key] = val
                elif key in ["Série BAC", "Année BAC", "Niveau Accès", "Annee Accès", "Voie Accès", "Académie"]:
                    result["academic_info"][key] = val
                elif key in ["Prof_Père", "Prof_Mère"]:
                    result["family_info"][key] = val
                else:
                    result["personal_info"][key] = val
    
    # Extract download links
    attestation = soup.find('a', href=re.compile(r'attestation-scolarite'))
    if attestation:
        result["download_links"]["attestation_scolarite"] = attestation.get('href', '')
    
    main_img = soup.find('img', width='100')
    if main_img and main_img.get('src'):
        result["basic_info"]["large_photo_url"] = main_img.get('src')
    
    # Extract section titles
    for h5 in soup.find_all('h5'):
        text = h5.get_text(strip=True)
        if "Situation Administrative" in text:
            result["sections"]["administrative"] = text
        elif "Données personnelles" in text:
            result["sections"]["personal"] = text
    
    return result