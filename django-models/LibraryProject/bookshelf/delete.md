### Delete Operation

**Command:**
```python
from bookshelf.models import Book
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()
all_books = Book.objects.all()
print(list(all_books))