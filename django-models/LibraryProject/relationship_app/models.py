from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    # ForeignKey: One Author can write many Books
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=200)
    # ManyToManyField: A Library can have many Books, and a Book can be in many Libraries
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # OneToOneField: A Librarian manages one Library, and a Library has one Librarian
    library = models.OneToOneField(Library, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name