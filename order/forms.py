from datetime import date
from .models import Order
from django.forms import ModelForm, TextInput, FileInput, DateTimeInput, Select,DateTimeField
from django import forms


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ("user", "book", "plated_end_at")
        widgets = {
            "user": Select(attrs={'class': 'form-control', 'placeholder': 'Select User'}),
            "book": Select(attrs={'class': 'form-control', 'placeholder': 'Select Book'}),
            "plated_end_at": DateTimeInput(attrs={'class': 'form-control', 'type':'datetime-local'})
        }


    def __init__(self,*args, **kwargs):
        super(OrderForm, self).__init__(*args,**kwargs)
        self.fields["user"].empty_label = "Select User"
        self.fields["book"].empty_label = "Select Book"

