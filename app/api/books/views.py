from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from books.models import Book

@login_required(login_url='/accounts/login/')
def books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'pages/books.html', context)

@login_required(login_url='/accounts/login/')
def book_info(request, id):
    book = Book.objects.get(id=id)
    context = {
        'book': book
    }
    return render(request, 'pages/book-info.html', context)