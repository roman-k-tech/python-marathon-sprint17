from django.urls import path, include
from . import views

urlpatterns =\
[
    path('orders', views.orders, name='orders'),
    path('orders/delete/<int:order_id>/', views.delete_order)
]