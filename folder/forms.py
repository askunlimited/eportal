from django import forms
from .models import Folder

from userprofiles.models import Department


class AddFolderForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control", "id":"name"})
    )

    description = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control", "id":"description"})
    )

    department = forms.ModelChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs={"class":"form-control", "id":"department"}))

    class Meta:
        model = Folder
        fields = (
            "name",
            "description",
            "department",
        )
