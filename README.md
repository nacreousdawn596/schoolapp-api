# School App API

A Python library designed to make interacting with the School App platform a lot less painful. Instead of wrestling with session cookies and manual HTML scraping, this library gives you a clean, object-oriented way to access your grades, attendance, and profile data.

## Why This Exists
Browsing the School App web interface manually for updates is slow. If you want to build a custom dashboard, a grade tracker, or a notification bot, you need a reliable way to get that data programmatically. This library takes care of:
- **Authentication**: Solid session management with automatic CSRF token handling.
- **Data Cleanup**: Converts messy HTML tables into structured Python objects.
- **Smart Logic**: Handles nested modules, element-level statistics, and transcript parsing out of the box.

## Quick Start

### Installation
You can install the library locally using:
```bash
pip install schoolapp-api
```

### Basic Usage
Getting your data is as simple as this:

```python
from schoolapp_api import SchoolAppClient

# Initialize and log in
client = SchoolAppClient()
if client.login("your.email@example.com", "password"):
    
    # Get your basic info
    profile = client.get_profile()
    print(f"Hello, {profile.full_name}!")
    
    # Fetch your current semester grades
    grades = client.get_current_elem_note()
    for item in grades:
        print(f"{item.CodeElem}: {item.Moy}")
```

## Project Layout
The library is organized into several specific managers, so you always know where to find what you need:

- **`grades`**: Handle module marks, element notes, and academic year results.
- **`attendance`**: Track your absences and see any sanctions.
- **`profile`**: Access your personal data and administrative files.
- **`courses`**: Browse the study plan and available modules.

For the full details on every class and function, head over to the [**/docs**](./docs/README.md) folder.

## Contributions
Found a bug or have an idea for a new feature? Feel free to open an issue or submit a pull request. Any help making this library better for everyone is appreciated!
