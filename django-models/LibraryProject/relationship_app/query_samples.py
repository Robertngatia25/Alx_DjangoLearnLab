# django-models/LibraryProject/relationship_app/query_samples.py

import os
import django

# --- Setup Django Environment ---
# This line sets the DJANGO_SETTINGS_MODULE environment variable
# to point to your project's settings file.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# --- Import your models ---
from relationship_app.models import Author, Book, Library, Librarian

# --- 1. Create Sample Data (Run this section only once) ---
print("--- Creating Sample Data ---")

# Create Authors
author1, created = Author.objects.get(name="Jane Austen")
print(f"Author: {author1.name} (Created: {created})")

author2, created = Author.objects.get(name="J.K. Rowling")
print(f"Author: {author2.name} (Created: {created})")

# Create Books
book1, created = Book.objects.get(title="Pride and Prejudice", author=author1)
print(f"Book: {book1.title} (Created: {created})")

book2, created = Book.objects.get(title="Harry Potter and the Sorcerer's Stone", author=author2)
print(f"Book: {book2.title} (Created: {created})")

book3, created = Book.objects.get(title="Emma", author=author1)
print(f"Book: {book3.title} (Created: {created})")

# Create Libraries
library1, created = Library.objects.get(name="Central Library")
if created: # Only add books if the library was just created to avoid duplicates
    library1.books.add(book1, book2) # Add books to the ManyToMany relationship
    library1.save()
print(f"Library: {library1.name} (Created: {created}, Books: {list(library1.books.all())})")

library2, created = Library.objects.get(name="Community Hub Library")
if created: # Only add books if the library was just created
    library2.books.add(book3)
    library2.save()
print(f"Library: {library2.name} (Created: {created}, Books: {list(library2.books.all())})")

# Create Librarians
# Note: For OneToOneField with primary_key=True, ensure the related object exists
librarian1, created = Librarian.objects.get(name="Alice Smith", library=library1)
print(f"Librarian: {librarian1.name} (Created: {created})")

librarian2, created = Librarian.objects.get(name="Bob Johnson", library=library2)
print(f"Librarian: {librarian2.name} (Created: {created})")


# --- Performing Queries ---
print("\n--- Performing Queries ---")

# --- Query 1: All books by a specific author ---
print("\nQuery 1: All books by Jane Austen")
try:
    jane_austen = Author.objects.get(name="Jane Austen")
    books_by_jane = Book.objects.filter(author=jane_austen) # or jane_austen.books.all()
    for book in books_by_jane:
        print(f"- {book.title} by {book.author.name}")
except Author.DoesNotExist:
    print("Jane Austen not found.")


# --- Query 2: List all books in a library ---
print("\nQuery 2: All books in Central Library")
# --- MODIFIED LINE START ---
library_name_central = "Central Library" # Define a variable for the library name
try:
    central_library = Library.objects.get(name=library_name_central) # Use the variable here
    books_in_central = central_library.books.all()
    for book in books_in_central:
        print(f"- {book.title} ({book.author.name})")
except Library.DoesNotExist:
    print(f"{library_name_central} not found.")
# --- MODIFIED LINE END ---


# --- Query 3: Retrieve the librarian for a library ---
print("\nQuery 3: Librarian for Community Hub Library")
# --- MODIFIED LINE START ---
library_name_community = "Community Hub Library" # Define a variable for the library name
try:
    community_library = Library.objects.get(name=library_name_community) # Use the variable here
    librarian_for_community = community_library.librarian # Access via the OneToOne relationship
    print(f"The librarian for {community_library.name} is {librarian_for_community.name}")
except Library.DoesNotExist:
    print(f"{library_name_community} not found.")
except Librarian.DoesNotExist:
    print(f"No librarian found for {community_library.name}")
# --- MODIFIED LINE END ---