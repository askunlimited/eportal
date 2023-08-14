from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm

from .forms import SignUpForm, LoginUserForm
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import User, Userprofile


# def signUp(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()

#             UserProfile.objects.create(user=user)
#             messages.success(request, "Account created, login to update your profile ")
#             return redirect(
#                 "signup"
#             )  # Replace 'home' with the URL name of your home page
#     else:
#         form = SignUpForm()

#     return render(request, "accounts/sign-up.html", {"form": form})


def signUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user=user)

            return redirect("dashboard")

    else:
        form = SignUpForm()

    return render(request, "accounts/sign-up.html", {"form": form})


def dashboard(request):
    return render(request, "accounts/dashboard.html")


def list_users(request):
    list_of_users = Userprofile.objects.filter()
    return render(request, "accounts/list_users.html", {"users": list_of_users})


# def log_In(request):
#     if request.method == "POST":
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get("email")
#             password = form.cleaned_data.get("password")

#             user = authenticate(email=email, password=password)

#             if user is not None:
#                 login(request, user)
#                 return redirect("dashboard")
#             else:
#                 messages.error(request, "Error")
#         else:
#             messages.error(request, "Email or Password incorrect")
#     form = LoginUserForm()
#     return render(request, "accounts/log-in.html", {"form": form})
