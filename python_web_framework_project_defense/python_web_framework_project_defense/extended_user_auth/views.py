from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from python_web_framework_project_defense.extended_user_auth.forms import SignInForm


def register(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to Login

    else:
        form = UserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'auth/register.html', context)


def log_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            # If form is valid, login the user and redirect to home page
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignInForm()

    context = {
        'form': form
    }

    return render(request, 'auth/login.html', context)


def log_out(request):
    logout(request)
    return redirect('index')


