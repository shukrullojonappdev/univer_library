from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from books.models import Book

@login_required(login_url='/accounts/login/')
def home(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    print(context)
    return render(request, 'pages/home.html', context)