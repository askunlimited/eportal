from django import forms
from .models import Document


class AddDocumentForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    description = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    # upload = forms.FileField(
    #     max_length=150, widget=forms.FileField(attrs={"class": "form-control"})
    # )

    class Meta:
        model = Document
        fields = (
            "name",
            "description",
            # "created_by",
        )
