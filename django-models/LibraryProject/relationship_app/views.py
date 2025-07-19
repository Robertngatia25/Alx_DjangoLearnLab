from django.shortcuts import render
from django.views.generic.detail import DetailView 
from .models import Library, Book

# --- 1. Function-based View: List all books ---
def book_list(request):
    # Retrieve all Book objects from the database
    books = Book.objects.all()
    # Render the 'list_books.html' template, passing the 'books' QuerySet as context
    return render(request, 'relationship_app/list_books.html', {'books': books})

# --- 2. Class-based View: Display details for a specific library ---
# DetailView is used to display a single object's details.
class LibraryDetailView(DetailView):
    # Specify the model that this view will display details for
    model = Library
    # Specify the template to use for rendering
    template_name = 'relationship_app/library_detail.html'
    # Optional: Change the context variable name from 'object' to 'library' for clarity in template
    context_object_name = 'library'

    # Note: DetailView automatically fetches the object based on the 'pk' (primary key)
    # or 'slug' provided in the URL. We'll use 'pk'.

    # You might also want to add extra context if needed, e.g.:
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # The 'object' (or 'library' due to context_object_name) is already in context
    #     # context['some_other_data'] = SomeOtherModel.objects.all()
    #     return context