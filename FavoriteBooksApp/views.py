from django.shortcuts import render, redirect
from .models import *


def home(request):
    if request.method == "POST":
        Book.create_book(request)
        return redirect('/books')
    else:
        context = {
            'all_books': Book.get_all_books()
        }
        return render(request, 'home.html', context=context)


def destroy(request):
    del request.session['userid']
    return redirect('/')


def books(request, id):
    context = {
        'books': Book.get_book_by_id(id),
        'book_liked_by_users': Book.objects.get(id=id).favorite_book.all()
    }
    return render(request, 'books.html', context=context)


def addbooks(request, id):
    book_id = id
    user_id = int(request.session['userid'])
    Book.assign_user_to_book(user_id, book_id)
    return redirect('/books')
