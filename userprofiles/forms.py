from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Department, Userprofile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

        help_texts = {
            "username": None,
            "email": None,
            "password1": None,
            "password2": None,
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password1"].help_text = None


class AddDepartmentForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Department
        fields = ("name",)


class EditProfileForm(forms.ModelForm):
    # email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    telephone = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    department = forms.ModelChoiceField(queryset=Department.objects.all())

    profile_picture = forms.FileField()

    class Meta:
        model = Userprofile
        fields = (
            "first_name",
            "last_name",
            "telephone",
            "department",
            # "email",
            "profile_picture",
        )
