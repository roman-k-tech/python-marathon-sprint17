from django.shortcuts import render, redirect
from .models import Book
from order.models import Order


def books(request):
    return render(request, 'book/books.html', {'books': Book.objects.all()})


def book_item(request, book_id):
    book = Book.objects.get(pk=book_id)
    amount_left = book.count - Order.objects.filter(book=book_id, end_at=None).count()

    context = {'title': book.name, 'id': book.id, 'authors': book.authors.all(),
               'count': book.count, 'amount_left': amount_left}

    return render(request, 'book/book_details.html', context)
