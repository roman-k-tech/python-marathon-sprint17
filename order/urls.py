from django.urls import path, include
from . import views

urlpatterns =\
[
    path('orders', views.orders, name='orders'),
    path('orders/delete/<int:order_id>/', views.delete_order),
    path('orders/form', views.orders_form, name='create_orders'),
    path('orders/form/<int:order_id>/', views.orders_form, name='update_orders'),
]