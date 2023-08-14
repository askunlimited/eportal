from django.urls import path
from .views import register_user, login_user

urlpatterns = [
    path("signup/", register_user, name="signup"),
    path("login_user/", login_user, name="login"),
    # path("dashboard/", dashboard, name="dashboard"),
    # path("staff/", list_users, name="list_users"),
]
