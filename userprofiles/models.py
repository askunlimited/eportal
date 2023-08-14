from django.contrib.auth.models import User
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        User, related_name="user_departments", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Userprofile(models.Model):
    user = models.ForeignKey(
        User, related_name="user_profiles", on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    telephone = models.CharField(max_length=16)
    email = models.CharField(max_length=150)
    department = models.ManyToManyField(
        Department,
        related_name="user_department",
        default=1,
        unique=False,
        blank=True,
    )
    profile_picture = models.ImageField(upload_to="profile_pics/")

    def __str__(self):
        return self.first_name
