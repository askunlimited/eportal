from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update(
            {"class": "w-full mb-2 bg-gray-100 p-2", "placeholder": "Enter staff Email"}
        )

        # self.fields["first_name"].widget.attrs.update(
        #     {
        #         "class": "w-full mb-2 bg-gray-100 p-2",
        #         "placeholder": "Enter your name",
        #     }
        # )

        # self.fields["last_name"].widget.attrs.update(
        #     {
        #         "class": "w-full mb-2 bg-gray-100 p-2",
        #         "placeholder": "Enter your last name",
        #     }
        # )

        # self.fields["telephone"].widget.attrs.update(
        #     {
        #         "class": "w-full mb-2 bg-gray-100 p-2",
        #         "placeholder": "Enter Staff Telephone number",
        #     }
        # )

        # self.fields["department"].widget.attrs.update(
        #     {"class": "w-full mb-2 bg-gray-100 p-2", "placeholder": "Enter department"}
        # )

        self.fields["password1"].widget.attrs.update(
            {"class": "w-full mb-2 bg-gray-100 p-2", "placeholder": "Enter password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "w-full mb-2 bg-gray-100 p-2", "placeholder": "Confirm password"}
        )

    email = forms.EmailField(widget=forms.EmailInput)
    # first_name = forms.CharField(max_length=150)

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "email",
            # "first_name",
            "password1",
            "password2",
        ]


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update(
            {
                "class": "w-full mb-2 bg-gray-100 p-2",
                "placeholder": "Enter your email address",
            }
        )

        self.fields["password"].widget.attrs.update(
            {
                "class": "w-full mb-2 bg-gray-100 p-2",
                "placeholder": "Enter your password",
            }
        )

    class Meta:
        fields = ["email", "password"]
