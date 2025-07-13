### Delete Operation

**Command:**
```python
from bookshelf.models import Book
# Note: Assuming 'retrieved_book' variable exists from a previous step,
# or retrieve the book by ID if needed (e.g., book_to_delete = Book.objects.get(id=1))
retrieved_book.delete()
# Confirm deletion by trying to retrieve all books:
Book.objects.all()