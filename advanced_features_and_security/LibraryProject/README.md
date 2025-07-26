# LibraryProject

This is a basic Django project for a Library system, created as part of the Django development environment setup task.

## Setup Instructions

1. Ensure Python and pip are installed.
2. Install Django: `pip install django`
3. Run the development server: `python manage.py runserver`

"""
Permissions Setup:
- Permissions defined in the Book model (can_view, can_create, can_edit, can_delete)
- Groups:
  - Viewers: can view books
  - Editors: can view, add, and edit
  - Admins: all permissions including delete
Views are protected using @permission_required for access control.
"""
