# SchoolAppClient

The `SchoolAppClient` is the main entry point for interacting with the School App API. It orchestrates authentication and provides access to various managers.

## Class: `SchoolAppClient`

Defined in: [school_app_client.py](../schoolapp_api/school_app_client.py)

### Constructor

#### `__init__(self, base_url=BASE_URL)`
Initializes the client.
- **`base_url`**: The base URL of the School App (defaults to `BASE_URL` from `constants.py`).

### Attributes

- **`self.base_url`**: The base URL being used.
- **`self.http_client`**: An instance of `HTTPClient` for making requests.
- **`self.auth`**: An instance of `AuthManager` for handling login and CSRF.
- **`self.grades`**: Instance of `GradesManager`.
- **`self.attendance`**: Instance of `AttendanceManager`.
- **`self.profile`**: Instance of `ProfileManager`.
- **`self.courses`**: Instance of `CourseManager`.

### Methods

#### `login(self, email, password)`
Authenticates the user.
- **`email`**: User's email address.
- **`password`**: User's password.
- **Returns**: `True` if successful, `False` otherwise.

#### `get_profile(self)`
Retrieves the user profile.
- **Returns**: A `Profile` object.

#### `get_filieres(self)`
Retrieves the list of available majors/filieres.
- **Returns**: A list of `Filiere` objects.

#### `get_absences(self)`
Retrieves the user's absences.

#### `get_sanctions(self)`
Retrieves the user's sanctions.

#### `get_elem_note(self)`
Retrieves all element grades.

#### `get_current_elem_note(self)`
Retrieves only current element grades.

#### `get_mod_note(self)`
Retrieves all module grades.

#### `get_current_mod_note(self)`
Retrieves only current module grades.

#### `get_annee(self)`
Retrieves the list of academic years.

#### `get_semestre(self)`
Retrieves the list of semesters.

#### `get_modules(self, niveau, filiere, semestre, refresh_csrf=False)`
Retrieves modules for a specific configuration.
- **`niveau`**: Academic year/level.
- **`filiere`**: Major/Filiere.
- **`semestre`**: Semester.
- **`refresh_csrf`**: Whether to refresh the CSRF token before the request.
