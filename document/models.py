from django.db import models
from django.contrib.auth.models import User

from folder.models import Folder
from userprofiles.models import Userprofile


class Document(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.CharField(max_length=255)
    upload = models.FileField(max_length=None, upload_to="documents/%Y/%m/%d/")
    folder = models.ForeignKey(Folder, related_name="documents", on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, related_name="documents", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
