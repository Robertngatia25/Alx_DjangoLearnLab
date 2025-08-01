# django-models/LibraryProject/relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView, register
from . import views
from django.contrib.auth import views as auth_views

app_name = 'relationship_app' # Namespace for URLs, useful for reverse lookups

urlpatterns = [
   path('books/', list_books, name='list_books'),
   path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
   path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
   path('register/', views.register, name='register'),
   path('admin-view/', views.admin_view, name='admin_view'),
   path('librarian-view/', views.librarian_view, name='librarian_view'),
   path('member-view/', views.member_view, name='member_view'),
   path('add_book/', views.add_book, name='add_book'),
   path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
   path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

]