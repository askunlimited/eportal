from django import forms
from .models import Folder



class AddFolderForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    description = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Folder
        fields = (
            "name",
            "description",
        )
