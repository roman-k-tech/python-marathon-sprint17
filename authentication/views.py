from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import UserRegistrationForm
from order.models import Order


def users(request):
    return render(request, 'authentication/users.html', {'users': CustomUser.objects.all()})


def user_item(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    context = {'first_name': user.first_name, 'middle_name': user.middle_name, 'last_name': user.last_name,
               'id': user.id, 'email': user.email, 'role': user.role, 'is_active': user.is_active,
               'orders': Order.objects.filter(user=user_id) }

    return render(request, 'authentication/user_details.html', context)


def delete_user(request, user_id):
    CustomUser.delete_by_id(user_id)
    return redirect('users')



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'authentication/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'authentication/register.html', {'user_form': user_form})
