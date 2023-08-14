from django.contrib import admin

from .models import Userprofile, Department

# Register your models here.

admin.site.register(Userprofile)
admin.site.register(Department)
