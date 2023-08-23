from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    get_list_or_404,
)
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import SignUpForm, AddDepartmentForm, EditProfileForm
from .models import Userprofile, Department
from django.contrib.auth.models import User

# Create your views here.


@login_required(login_url="/")
def dashboard(request):
    return render(request, "userprofiles/dashboard.html")


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
            return redirect("login")
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
            return redirect("dashboard")
        else:
            messages.error(
                request, "There's an error logging in, check your login details"
            )
            return redirect("/")

    else:
        if request.user.is_authenticated:
            return redirect("dashboard")
        return render(request, "userprofiles/log-in.html", {})


def sign_out(request):
    """
    Basic view for user sign out
    """
    logout(request)
    return redirect("/")


@login_required(login_url="/")
def list_department(request):
    
    departments = Department.objects.all()
    user = User.objects.get(id=request.user.id)
    print("USER: ", user)
    userp = user.user_profiles.get()
    print(userp.department)

    form = AddDepartmentForm()

    return render(
        request, "userprofiles/list_department.html", {"departments": departments, "form":form}
    )


@login_required(login_url="/")
def add_department(request):
    if request.method == "POST":
        form = AddDepartmentForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            department.created_by = request.user
            department.save()
            messages.success(request, "Department added successfully")
            return redirect("all_departments")
        else:
            messages.error(request, "Department not created, try again")
    else:
        form = AddDepartmentForm()
    return render(request, "userprofiles/add_department.html", {"form": form})


@login_required(login_url="/")
def edit_department(request, pk):
    department = get_object_or_404(Department, created_by=request.user, pk=pk)
    if request.method == "POST":
        form = AddDepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()

            messages.success(request, "Department edited successfully")
            return redirect("all_departments")
        else:
            messages.error(request, "Department not edited, try again")
    else:
        form = AddDepartmentForm(instance=department)
    return render(request, "userprofiles/add_department.html", {"form": form})


@login_required(login_url="/")
def delete_department(request, pk):
    department = get_object_or_404(Department, created_by=request.user, pk=pk)
    department.delete()
    return redirect("all_departments")


# Userprofiles


@login_required(login_url="/")
def list_users(request):
    userprofiles = Userprofile.objects.all()

    return render(
        request, "userprofiles/list_users.html", {"userprofiles": userprofiles}
    )


@login_required(login_url="/")
def edit_userprofile(request, pk):
    userprofile = get_object_or_404(Userprofile, pk=pk)
    if request.method == "POST":
        form = EditProfileForm(
            request.POST or None, request.FILES or None, instance=userprofile
        )
        if form.is_valid():
            form.save()

            messages.success(request, "Profile edited successfully")
            return redirect("dashboard")
        else:
            messages.error(request, "Profile not edited, try again")
    else:
        form = EditProfileForm(instance=userprofile)
    return render(request, "userprofiles/edit_userprofile.html", {"form": form})
