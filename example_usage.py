"""
Example usage of the refactored SchoolAppClient
"""
from schoolapp_api import SchoolAppClient


def main():
    # Initialize client
    client = SchoolAppClient()
    
    # Login
    email = "your.email@example.com"
    password = "your_password"
    
    if client.login(email, password):
        print("\n✓ Login successful!\n")
        
        # Get filieres
        filieres_html = client.get_filieres()
        if filieres_html:
            print("✓ Fetched filieres successfully\n")
        
        # Get modules for specific niveau/filiere/semestre
        content = client.get_modules(
            niveau="1A",
            filiere="API-MPT",
            semestre="S1"
        )
        if content:
            print("✓ Fetched modules successfully")
            print(content)        
        # If you get 403 errors, try with refresh_csrf=True
        # modules_html = client.get_modules(
        #     niveau="1A",
        #     filiere="API-MPT",
        #     semestre="S1",
        #     refresh_csrf=True
        # )
    else:
        print("✗ Login failed!")


if __name__ == "__main__":
    main()
