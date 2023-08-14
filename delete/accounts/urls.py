from django.urls import path
from .views import signUp, dashboard, list_users

urlpatterns = [
    path("signup/", signUp, name="signup"),
    path("dashboard/", dashboard, name="dashboard"),
    path("staff/", list_users, name="list_users"),
]
