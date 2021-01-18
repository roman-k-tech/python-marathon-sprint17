from django.forms import ModelForm, TextInput
from .models import Author


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']
        widgets = {
            "name": TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}),
            "surname": TextInput(attrs={'class': 'form-control', 'placeholder': 'surname'}),
            "patronymic": TextInput(attrs={'class': 'form-control', 'placeholder': 'patronymic'}),
            "books": TextInput(attrs={ 'class': 'form-control', 'placeholder': 'books' })
        }
