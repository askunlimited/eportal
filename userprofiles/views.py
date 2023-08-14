from django.shortcuts import render, redirect

# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Userprofile
from django.contrib import messages

from .forms import SignUpForm
from .models import Userprofile

# Create your views here.


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(
                user=user,
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
            )
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("signup")
    else:
        form = SignUpForm()
    return render(request, "userprofiles/sign-up.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("signup")
        else:
            messages.error(
                request, "There's an error logging in, check your login details"
            )
            return redirect("login")

    else:
        return render(request, "userprofiles/log-in.html", {})
