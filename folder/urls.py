from django.urls import path

from .views import add_folder, list_folder, edit_folder, delete_folder, folder_document, add_folder_document, view_document

urlpatterns = [
    path("", list_folder, name="all_folders"),
    path("add/", add_folder, name="add_folder"),
    path("edit/", edit_folder, name="edit_folder"),
    path("<int:pk>/delete/", delete_folder, name="delete_folder"),
    path("document/<int:pk>/", folder_document, name="folder_document"),
    path("document/<int:pk>/view/", view_document, name="view_document"),
    path("document/add/", add_folder_document, name="add_folder_document"),
]
