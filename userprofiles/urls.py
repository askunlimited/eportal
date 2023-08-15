from django.urls import path
from .views import (
    register_user,
    login_user,
    add_department,
    dashboard,
    edit_department,
    list_department,
    delete_department,
    edit_userprofile,
    list_users,
    sign_out,
)

urlpatterns = [
    path("signup/", register_user, name="signup"),
    path("", login_user, name="login"),
    path("log-out/", sign_out, name="log-out"),
    path("add_department/", add_department, name="add_dept"),
    path("department/<int:pk>/edit/", edit_department, name="edit_dept"),
    path("department/<int:pk>/delete/", delete_department, name="delete_dept"),
    path("dashboard/", dashboard, name="dashboard"),
    path("departments/", list_department, name="list_dept"),
    path("userprofile/<int:pk>/edit/", edit_userprofile, name="edit_profile"),
    path("userprofiles/", list_users, name="list_users"),
    # path("staff/", list_users, name="list_users"),
]
