from django.urls import path, include
from . import views

urlpatterns =\
[
    path('users/', views.users, name='users'),
    path('users/<int:user_id>/', views.user_item, name='user_item'),
    path('users/delete/<int:user_id>/', views.delete_user)
]