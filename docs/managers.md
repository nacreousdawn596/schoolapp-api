# Managers

Managers handle specific domains of the School App API, such as grades, attendance, profile, and courses. They all inherit from a common `BaseManager`.

## `BaseManager`

The foundation for all other managers.

### Attributes
- **`client`**: Reference to the `SchoolAppClient`.
- **`http_client`**: Reference to the `HTTPClient` from the main client.
- **`auth`**: Reference to the `AuthManager` from the main client.

### Methods
- **`ensure_logged_in(self)`**: Checks if the user is authenticated.
- **`get_json_or_parse(self, url, parser, params=None, refresh_csrf=True)`**: A helper method that fetches a URL, updates the CSRF token, and uses a parser to return structured data.

---

## `GradesManager`

Handles student grades and academic results. Inherits from `BaseManager`.

### Methods
- **`get_element_notes(self, current=False)`**: Fetches element-level grades.
    - `current`: If `True`, fetches only current/in-progress grades.
    - Returns: List of `Element` objects.
- **`get_module_notes(self, current=False)`**: Fetches module-level grades.
    - `current`: If `True`, fetches only current/in-progress grades.
    - Returns: List of `Module` objects.
- **`get_years(self)`**: Fetches academic years.
    - Returns: List of `Annee` objects.
- **`get_semesters(self)`**: Fetches semesters.
    - Returns: List of `Semestre` objects.

---

## `AttendanceManager`

Handles absences and sanctions. Inherits from `BaseManager`.

### Methods
- **`get_absences(self)`**: Fetches a summary of student absences.
- **`get_sanctions(self)`**: Fetches a list of student sanctions.

---

## `ProfileManager`

Handles student profile information and program listings. Inherits from `BaseManager`.

### Methods
- **`get_profile(self)`**: Fetches the student's profile information.
    - Returns: A `Profile` object (parsed by `parsers.profile`).
- **`get_filieres(self)`**: Fetches the list of available majors/filieres.

---

## `CourseManager`

Handles course-related data and study plans. Inherits from `BaseManager`.

### Methods
- **`get_modules(self, niveau, filiere, semestre, refresh_csrf=False)`**: Fetches modules for a specific configuration.
    - `niveau`: Academic level (e.g., 'CI1').
    - `filiere`: Major ID.
    - `semestre`: Semester ID.
    - `refresh_csrf`: If `True`, refreshes the CSRF token before making the request.
    - Returns: Parsed module data.
