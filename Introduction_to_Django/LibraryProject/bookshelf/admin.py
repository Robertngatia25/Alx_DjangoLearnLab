# bookshelf/admin.py

from django.contrib import admin
from .models import Book

# ----------------------------------------------------
# Define a custom ModelAdmin for the Book model
# ----------------------------------------------------

class BookAdmin(admin.ModelAdmin):
    # 1. Customize the list view display (fields shown in the table)
    list_display = ('title', 'author', 'publication_year')

    # 2. Add filters to the sidebar
    list_filter = ('publication_year', 'author')

    # 3. Add search capabilities (searches the specified fields)
    search_fields = ('title', 'author')

    # Optional: Order the list view by publication year descending
    ordering = ('-publication_year',)

# ----------------------------------------------------
# Register the Book model with the custom admin class
# ----------------------------------------------------

admin.site.register(Book, BookAdmin)