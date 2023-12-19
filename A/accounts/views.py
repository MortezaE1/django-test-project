from django.shortcuts import render, redirect
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'User login successfully...')
                return redirect('home')
            messages.error(request, 'Username or password is wrong...', 'danger')
            return redirect('login')
    else:
        form = LoginUserForm
    return render(request, 'login.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['username'], password=cd['password'], email=cd['email'],
                                     first_name=cd['first_name'], last_name=cd['last_name'])
            messages.success(request, 'user create successfully', 'success')
            return redirect('home')
    else:
        form = RegisterUserForm
    return render(request, 'register.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, 'logout user successfully', 'success')
    return redirect('login')
