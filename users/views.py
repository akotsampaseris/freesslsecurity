from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User
from .forms import LoginForm, RegisterForm, EditUserForm

# Create your views here.
@login_required
def dashboard(request):
    users = User.objects.all()

    context = {
        "users": users
    }

    return render(request, 'users/dashboard.html', context)

@login_required
def settings(request):
    user = request.user

    context = {
        "user": user
    }

    return render(request, 'users/settings.html', context)

def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('users:dashboard')

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password != confirm_password:
                messages.error(request, 'The passwords you provided do not match!')
                return redirect('users:register')

            try:
                user = form.save()
            except:
                return redirect('users:register', {"email": email})

            user.set_password(password)
            user.save()

            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome to FreeSSL Security!')
                return redirect('users:dashboard')
    else:
        form = RegisterForm()

    context = {
        "form": form
    }

    return render(request, 'users/register.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('users:dashboard')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'You have logged in successfully!')
                    return redirect('users:dashboard')
                else:
                    messages.error(request, 'Your account has been deactivated!')
                    return redirect('users:login')
            else:
                messages.error(request, 'The details you provided were wrong!')
                return redirect('users:login')
    else:
        form = LoginForm()

    context = {
        "form": form
    }

    return render(request, 'users/login.html', context)


@login_required
def logoutUser(request):
    logout(request)
    return redirect('pages:home')


def editUser(request, email):
    user = User.objects.get(email=email)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            new_password = form.cleaned_data['password']
            user.set_password(new_password)
            user.save()
            messages.success(request, 'You have successfully updated your password!')

            return redirect('users:dashboard')
        else:
            messages.error(request, 'There has been an error!')
            return redirect('users:edit')
    else:
        form = EditUserForm(instance=user)

    context = {
        "form": form
    }

    return render(request, 'users/edit.html', context)


def deleteUser(request, email):
    user = User.objects.get(email=email)
    user.delete()
    messages.success(request, 'The user was deleted successfully!')

    return redirect('users:dashboard')
