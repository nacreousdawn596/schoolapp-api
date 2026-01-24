# Data Types

The library uses a set of domain models to represent various school-related data. All data models inherit from `BaseType`.

## `BaseType`

The base class for all domain models. It dynamically maps dictionary keys from parsed data to object attributes.

### Attributes
- **`client`**: Reference to the `SchoolAppClient`.
- **`_stats`**: Internal cache for fetched statistics.

### Methods
- **`__init__(self, client, data)`**: Initializes the object and maps data keys to attributes. Cleans keys (e.g., replaces spaces with underscores).
- **`_ensure_logged_in(self)`**: Internal helper to check authentication.
- **`_get_stats(self, url, params)`**: Internal helper to fetch statistical data associated with the model.

---

## `Element`

Represents a module element (e.g., a specific subject) with its grades.

### Attributes
- Dynamically mapped from parsed data (e.g., `CodeElem`, `AU`, `CC`, `EX`, `TP`, `Moy`).

### Methods
- **`fetch_stats(self, eval_type)`**: Fetches statistics for a specific evaluation type (`NoteCC`, `NoteEX`, `NoteTP`, `MoyElem`).
- **`cc_stats`** (Property): Retrieves cached or fresh statistics for Continuous Control (CC).
- **`ex_stats`** (Property): Retrieves cached or fresh statistics for Exams (EX).
- **`tp_stats`** (Property): Retrieves cached or fresh statistics for Practical Work (TP).
- **`moy_stats`** (Property): Retrieves cached or fresh statistics for the Element Average (Moy).

---

## `Module`

Represents a course module, which is typically a collection of elements.

### Attributes
- Dynamically mapped (e.g., `CodeMod`, `AU`, `Moy`).

### Methods
- **`fetch_stats(self)`**: Fetches statistical distribution for the module average.
- **`stats`** (Property): Retrieves cached or fresh module statistics.

---

## `Annee`

Represents the results for an entire academic year.

### Attributes
- Dynamically mapped (e.g., `Niveau`, `Filiere`, `AU`, `Moy_Annee`).

### Methods
- **`fetch_stats(self)`**: Fetches statistical distribution for the year average.
- **`stats`** (Property): Retrieves cached or fresh year statistics.

---

## `Semestre`

Represents the results for a specific semester.

### Attributes
- Dynamically mapped (e.g., `Niveau`, `Filiere`, `Semestre`, `AU`, `Moy_SEM`).

### Methods
- **`fetch_stats(self)`**: Fetches statistical distribution for the semester average.
- **`stats`** (Property): Retrieves cached or fresh semester statistics.
