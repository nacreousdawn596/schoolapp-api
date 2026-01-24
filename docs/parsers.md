# Parsers

The library uses specialized parsers to extract structured data from the HTML responses of the School App. These are internal utilities but are documented here for transparency.

## Common Interface

All parsers follow a simple functional interface:
- **`parse(html_content)`**: Takes a string of HTML and returns a dictionary or a list of dictionaries.

---

## `parsers.profile`

Extracts detailed student profile information from the index page.

### Extracted Data Structure
- **`basic_info`**: Photo URLs, full name, role, and welcome message.
- **`administrative_info`**: Data from the situation administrative table.
- **`personal_info`**: CIN, date of birth, nationality, etc.
- **`contact_info`**: Email, phone, parents' contact details.
- **`academic_info`**: BAC details, access level, year of entry.
- **`download_links`**: URLs for documents like "Attestation de Scolarité".

---

## `parsers.absences`

Parses the absences and sanctions page.

### Extracted Data Structure
- **`summary`**: List of elements with total justified and non-justified absences.
- **`details`**: Detailed list of absence events (date, session, justification status, remarks).
- **`semestre`**: The current semester identifier (e.g., "S1").

---

## `parsers.note_elem`

Extracts element-level grades (Continuous Control, Exams, etc.).

### Extracted Data Structure
Returns a list of dictionaries, each containing:
- `CodeElem`, `AU`, `CC`, `EX`, `TP`, `MoySO`, `RAT`, `MoySR`, `Moy`, `Dec`.
- Numeric values are automatically converted to floats.

---

## `parsers.modules`

Parses the study plan view, which includes modules and their nested elements.

### Extracted Data Structure
Returns a dictionary keyed by module code. Each module includes:
- Attributes: `intitule`, `niveau`, `semestre`, `vhmod`, `coef`, `seuil`, `eliminatoire`.
- **`elements`**: A list of nested elements, each with its own codes, titles, hourly volume (VH), and coefficients.

---

## `parsers.stats`

Extracts statistical distribution data from modal popups.

### Extracted Data Structure
Returns a dictionary containing:
- `Votre_note`, `Moyenne_promo`, `Max`, `Min`, `Ecart_type`, `Effectif`, `Votre_classement`.
