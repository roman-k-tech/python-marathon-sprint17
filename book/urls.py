from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns =\
[
    path('', views.books, name='books'),
    path('books/', views.books, name='books'),
    path('books/<int:book_id>/', views.book_item, name='book_item')
]