# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
# from django.utils import timezone


# # Create your models here.
# class CustomUserManager(UserManager):
#     def _create_user(self, email, password, **extra_fields):
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)

#         return user

#     def create_user(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         return self._create_user(email, password, **extra_fields)


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(blank=True, default="", unique=True)
#     first_name = models.CharField(max_length=255, blank=True, default="")
#     # last_name = models.CharField(max_length=255, blank=True, default="")
#     # telephone = models.CharField(max_length=255, blank=True, default="")
#     # department = models.CharField(max_length=255, blank=True, default="")
#     # department = models.ForeignKey(deprtment.Department, on_delete=models.DO_NOTHING)

#     is_active = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)

#     date_joined = models.DateTimeField(default=timezone.now)
#     last_login = models.DateTimeField(blank=True, null=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = "email"
#     EMAIL_FIELD = "email"
#     REQUIRED_FIELDS = []

#     class Meta:
#         verbose_name = "User"
#         verbose_name_plural = "Users"

#     def get_full_name(self):
#         return self.first_name

#     def get_short_name(self):
#         return self.first_name

# from django.db import models
# from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.models import AbstractUser


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password, **extra_fields):
#         email = self.normalize_email(email)

#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must be a staff")

#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have superuser set to true")

#         return self.create_user(email=email, password=password, **extra_fields)


# class User(AbstractUser):
#     email = models.CharField(max_length=255, unique=True)
#     # first_name = models.CharField(max_length=255)

#     objects = CustomUserManager()

#     USERNAME_FIELD = "email"
#     # EMAIL_FIELD = "email"
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email


from django.contrib.auth.models import User
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description: models.CharField(max_length=255, blank=True, null=True)
    staff = models.ManyToManyField(User, related_name="staff")
    # folder = models.ManyToManyField(Folder, related_name="departments")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Userprofile(models.Model):
    user = models.OneToOneField(
        User, related_name="user_profiles", on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=255, blank=True, default="")
    last_name = models.CharField(max_length=255, blank=True, default="")
    telephone = models.CharField(max_length=255, blank=True, default="")
    is_active = models.BooleanField(default=True)
    profile_picture = models.ImageField(upload_to="media", blank=True, default="")
    department = models.ForeignKey(
        Department, related_name="staffs", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.first_name


# class UserProfile(models.Model):
#     user = models.ForeignKey(User, related_name="userprofile", on_delete=models.CASCADE)
#     # email = models.EmailField(blank=True, default="", unique=True)
