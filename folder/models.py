from django.db import models

from userprofiles.models import Userprofile


class Folder(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=True)
    # department = models.ManyToManyField(Department, related_name="folders")
    created_by = models.ForeignKey(
        Userprofile, related_name="folders", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
