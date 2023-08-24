from django.urls import path

from .views import add_folder, list_folder, edit_folder, delete_folder

urlpatterns = [
    path("", list_folder, name="all_folders"),
    path("add/", add_folder, name="add_folder"),
    path("folder/edit/", edit_folder, name="edit_folder"),
    # path("folder/<int:pk>/edit/", edit_folder, name="edit_folder"),
    path("folder/<int:pk>/delete/", delete_folder, name="delete_folder"),
]
