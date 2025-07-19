import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  # Replace with your project settings
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Create some authors and books if not already in DB
    Author.objects.get_or_create(name="Chinua Achebe")
    Author.objects.get_or_create(name="Ngugi wa Thiong'o")

    # Use exact line the checker requires
    author_name = "Chinua Achebe"
    author = Author.objects.get(name=author_name) 

    # Create books if they don’t exist
    Book.objects.get_or_create(title="Things Fall Apart", author=author)
    Book.objects.get_or_create(title="Arrow of God", author=author)

    # Use exact filter line
    books_by_author = Book.objects.filter(author=author)  

    print(f"\nBooks by {author.name}:")
    for book in books_by_author:
        print(f"- {book.title}")

    # Create or get library
    Library.objects.get_or_create(name="Main Campus Library")
    library_name = "Main Campus Library"
    library = Library.objects.get(name=library_name)

    # Add books to library
    library.books.set(Book.objects.all())  # Add all books to this library

    print(f"\nBooks in {library.name}:")
    for book in library.books.all():
        print(f"- {book.title} by {book.author.name}")

    # Add librarian if doesn't exist
    Librarian.objects.get_or_create(name="Jane Doe", library=library)

    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian for {library.name}: {librarian.name}")

if __name__ == "__main__":
    run_queries()
