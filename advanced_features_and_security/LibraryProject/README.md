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
# Security Measures in Django Project

## settings.py
- Enforced browser-side protections
- Enabled secure cookies
- Disabled DEBUG in production

## Templates
- Added {% csrf_token %} in all forms

## Views
- All queries use Django ORM
- Inputs are validated using Django forms

## CSP
- Implemented via django-csp to reduce XSS risk
