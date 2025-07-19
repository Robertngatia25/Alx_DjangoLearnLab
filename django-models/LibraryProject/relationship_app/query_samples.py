import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')  # replace with your project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Create some data
    author1 = Author.objects.create(name="Chinua Achebe")
    author2 = Author.objects.create(name="Ngugi wa Thiong'o")

    book1 = Book.objects.create(title="Things Fall Apart", author=author1)
    book2 = Book.objects.create(title="Arrow of God", author=author1)
    book3 = Book.objects.create(title="The River Between", author=author2)

    library = Library.objects.create(name="Main Campus Library")
    library.books.set([book1, book2, book3])  # ManyToMany add

    librarian = Librarian.objects.create(name="Jane Doe", library=library)

    # 1. Query all books by a specific author
    print(f"\nBooks by {author1.name}:")
    for book in Book.objects.filter(author=author1):
        print(f"- {book.title}")

    # 2. List all books in a library
    print(f"\nBooks in {library.name}:")
    for book in library.books.all():
        print(f"- {book.title} by {book.author.name}")

    # 3. Retrieve the librarian for a library
    librarian_for_library = Librarian.objects.get(library=library)
    print(f"\nLibrarian for {library.name}: {librarian_for_library.name}")

if __name__ == "__main__":
    run_queries()
