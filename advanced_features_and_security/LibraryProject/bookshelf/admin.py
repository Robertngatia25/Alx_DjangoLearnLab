from django.contrib import admin
from .models import Book
# Register your models here.
# ----------------------------------------------------
# Define a custom ModelAdmin for the Book model
# This class tells Django how to display and manage the Book model in the admin
# ----------------------------------------------------

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','publication_year')

    # 2. Configure list filters:
    #    This creates filters in the right sidebar of the change list page.
    list_filter = ('publication_year', 'author') # You can filter by these fields

    # 3. Add search capabilities:
    #    This adds a search bar that searches within the specified fields.
    search_fields = ('title', 'author') # You can search by title or author

    # Optional: You can also add ordering for the list view
    ordering = ('-publication_year', 'title') # Orders by year descending, then title ascending

# ----------------------------------------------------
# Register the Book model with the custom admin class
# ----------------------------------------------------
admin.site.register(Book, BookAdmin)
