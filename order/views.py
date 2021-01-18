from django.shortcuts import render
from .models import Order


def orders(request):
    return render(request, 'order/orders.html', {'orders': Order.objects.all()})


def order_item(request, order_id):
    order = Order.objects.get(pk=order_id)
    context = {'user': order.user, 'book': order.book, 'created_at': order.created_at,
               'end_at': order.end_at, 'plated_end_at': order.plated_end_at
               }

    return render(request, 'order/order_details.html', context)