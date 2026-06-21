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

            raw = {}
            for row in rows:
                th, td = row.find('th'), row.find('td')
                if th and td:
                    raw[th.get_text(strip=True)] = td.get_text(strip=True)

            # Validate BEFORE renaming keys — this was the bug: the old code
            # checked expected_keys (with spaces) against a dict whose keys
            # had already been rewritten to use underscores, so the check
            # could never pass and the function always returned {}.
            if not all(k in raw for k in expected_keys):
                continue

            stats = {}
            for key, val in raw.items():
                clean_key = key.replace(" ", "_")
                try:
                    if key in ["Effectif", "Votre classement"]:
                        stats[clean_key] = int(float(val))
                    elif key in ["Votre note", "Moyenne promo", "Max", "Min", "Ecart type"]:
                        stats[clean_key] = float(val)
                    else:
                        stats[clean_key] = val
                except (ValueError, TypeError):
                    stats[clean_key] = val

            return stats

    return {}