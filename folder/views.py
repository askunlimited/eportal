from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import AddFolderForm
from .models import Folder
from userprofiles.models import Department, Userprofile
from document.models import Document
from document.forms import AddDocumentForm

# Create your views here.

@login_required(login_url="/")
def list_folder(request):
    form = AddFolderForm()
    # print("CURRENT USER DEPARTMENT: ",current_user.department)
    if not request.user.is_staff:
        current_user = Userprofile.objects.get(user=request.user.id)
        current_user_id = current_user.department.id
        folders  = Folder.objects.filter(department=current_user_id)
        # folders = Folder.objects.filter()
        return render(request, "folder/list_folder.html", { "folders": folders, "form":form })
    # print(folders.department)
    folders = Folder.objects.all()
    return render(request, "folder/list_folder.html", { "folders": folders, "form":form })

@login_required(login_url="/")
def add_folder(request):
    if request.method == "POST":
        form = AddFolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.created_by = request.user
            folder.save()
            messages.success(request, "Folder added successfully")
            return redirect("all_folders")
        else:
            messages.error(request, "Folder not created, try again")
    else:
        form = AddFolderForm()
    return render(request, "folder/add_folder.html", {"form": form})

@login_required(login_url="/")
def edit_folder(request):
    pk = request.POST["id"]
    folder = Folder.objects.get(pk=pk)
    # folder = get_object_or_404(Folder, pk=pk)
    if request.method == "POST":
        form = AddFolderForm(request.POST, instance=folder)
        if form.is_valid():
            form.save()

            messages.success(request, "Folder edited successfully")
            return redirect("all_folders")
        else:
            messages.error(request, "Folder not edited, try again")
    else:
        form = AddFolderForm(instance=folder)
    return render(request, "folder/add_folder.html", {"form": form})

@login_required(login_url="/")
def delete_folder(request, pk):
    folder = Folder.objects.get(pk=pk)
    # folder = get_object_or_404(Folder, pk=pk)
    folder.delete()
    return redirect("all_folders")


def folder_document(request, pk):
    folder = Folder.objects.get(pk=pk)
    documents = Document.objects.filter(folder=pk)
    form = AddDocumentForm()
    context = {
        "folder": folder,
        "documents": documents,
        "form": form
    }
    return render(request, "folder/folder_document.html", context)

def add_folder_document(request):
    if request.method == "POST":
        form = AddDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.created_by = request.user
            document.save()
            messages.success(request, "document added successfully")
            return redirect("all_folders")
        else:
            messages.error(request, "document not created, try again")
    else:
        messages.error(request, "Method not allowed")
        return redirect('folder_document')

def view_document(request, pk):
    document = Document.objects.get(pk=pk)
    context = {
        "document": document
    }
    return render(request, "folder/view_document.html", context)