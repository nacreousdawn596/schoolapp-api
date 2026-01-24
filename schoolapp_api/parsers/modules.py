from bs4 import BeautifulSoup

def parse(html_content):
    """Parse HTML content containing modules and their elements."""
    soup = BeautifulSoup(html_content, "html.parser")
    modules = {}

    main_table = soup.find("table", class_="table table-striped table-sm mb-1 display")
    if not main_table:
        return {} # Return empty instead of raising error for robustness

    tbody = main_table.find("tbody")
    if not tbody:
        return {}
        
    rows = tbody.find_all("tr", recursive=False)
    current_mod = None

    for row in rows:
        classes = row.get("class", [])

        if "clickable" in classes:
            cols = row.find_all("td")
            if len(cols) >= 10:
                current_mod = cols[1].text.strip()
                modules[current_mod] = {
                    "intitule": cols[2].text.strip(),
                    "niveau": cols[4].text.strip(),
                    "semestre": cols[5].text.strip(),
                    "vhmod": int(cols[6].text.strip() or 0),
                    "coef": float(cols[7].text.strip() or 0),
                    "seuil": float(cols[8].text.strip() or 0),
                    "eliminatoire": float(cols[9].text.strip() or 0),
                    "elements": []
                }
        elif "collapse" in classes and current_mod:
            inner_table = row.find("table")
            if inner_table and inner_table.find("tbody"):
                for erow in inner_table.find("tbody").find_all("tr"):
                    ecol = erow.find_all("td")
                    if len(ecol) >= 10:
                        modules[current_mod]["elements"].append({
                            "code": ecol[0].text.strip(),
                            "intitule": ecol[1].text.strip(),
                            "vh_ctd": int(ecol[2].text.strip() or 0),
                            "vh_tp": int(ecol[3].text.strip() or 0),
                            "vh_eval": int(ecol[4].text.strip() or 0),
                            "coef_cc": float(ecol[5].text.strip() or 0),
                            "coef_ex": float(ecol[6].text.strip() or 0),
                            "coef_ecrit": float(ecol[7].text.strip() or 0),
                            "coef_tp": float(ecol[8].text.strip() or 0),
                            "coef_elem": float(ecol[9].text.strip() or 0),
                        })

    return modules
