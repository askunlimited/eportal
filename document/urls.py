from django.urls import path

from .views import (
    add_document,
    list_document,
    edit_document,
    delete_document,
    detail_document,
)

urlpatterns = [
    path("", list_document, name="all_documents"),
    path("add/", add_document, name="add_document"),
    path("document/<int:pk>/edit/", edit_document, name="edit_document"),
    path("document/<int:pk>/delete/", delete_document, name="edit_document"),
    path("document/<int:pk>/", detail_document, name="detail_document"),
]
