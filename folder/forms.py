from django import forms
from .models import Folder

from userprofiles.models import Department


class AddFolderForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    description = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    department = forms.ModelChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))

    class Meta:
        model = Folder
        fields = (
            "name",
            "description",
            "department",
        )
