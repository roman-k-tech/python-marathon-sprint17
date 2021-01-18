from django.urls import path, include
from . import views

urlpatterns =\
[
    path('authors/', views.authors, name='authors'),
    path('authors/<int:author_id>/', views.author_item, name='author_item')
]