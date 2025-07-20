from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView 
from .models import Library, Book
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def list_books(request):
    books = Book.objects.all()
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

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Redirect to homepage or dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})