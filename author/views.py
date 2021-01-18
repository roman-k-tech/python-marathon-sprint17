from django.shortcuts import render, redirect
from .models import Author


def authors(request):
    return render(request, 'author/authors.html', {'authors': Author.objects.all()})


def author_item(request, author_id):
    author = Author.objects.get(pk=author_id)
    context = {'name': author.name, 'surname': author.surname,
               'id': author.id, 'books': author.books.all()}
    return render(request, 'author/author_details.html', context)
