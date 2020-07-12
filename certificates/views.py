from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from users.models import User

# Create your views here.
@login_required
def dashboard(request):
    users = User.objects.all()

    context = {
        "users": users
    }

    return render(request, 'certificates/dashboard.html', context)
