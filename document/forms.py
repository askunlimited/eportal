from django import forms
from .models import Document
from .models import Folder


class AddDocumentForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    description = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    folder = forms.ModelChoiceField(queryset=Folder.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))

    upload = forms.FileField()

    class Meta:
        model = Document
        fields = (
            "name",
            "description",
            "folder",
            "upload",
            # "created_by",
        )
        # widget = {
        #     'file' : forms.FileInput(attrs={'class': 'form-control',
        #                                      'id' : 'input-file'}),
        #     }
