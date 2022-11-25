from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .models import *

menu = [{'title': 'Main Page', 'url_name': 'home'},
        {'title': 'Registration', 'url_name': 'registration'},
        {'title': 'Sing_in', 'url_name': 'sing_in'},
        ]


def index(request):
    info = Users.objects.all()
    return render(request, 'bank/index.html', {'menu': menu, 'title': 'Main Page', 'info': info})


def user_page(request):
    info = Users.objects.all()
    return render(request, 'bank/user_page.html', {'menu': menu, 'title': 'User_page', 'info': info})


# def registration(request):
#     if request.method == 'POST':
#         form = AddUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddUserForm()
#     return render(request, 'bank/registration.html', {'form': form, 'menu': menu, 'title': 'registration'})


def sing_in(request):
    return render(request, 'bank/sing_in.html')


def transfer(request):
    return render(request, 'bank/transfer.html')


def bringing_in(request):
    return render(request, 'bank/bringing_in.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('ERRORRRRR')


class RegisterUser(CreateView):
    form_class = RegistrationUserForm
    template_name = 'bank/registration.html'
    success_url = reverse_lazy('user')
    extra_context = {'menu': menu}

# class LoginUser(LoginView):
#     form_class = AuthenticationForm
#     template_name = 'bank/register.html'
