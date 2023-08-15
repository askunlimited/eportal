from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from django.contrib import messages

from .forms import AddFolderForm
from .models import Folder

# Create your views here.


def list_folder(request):
    folders = Folder.objects.all()
    # folders = get_list_or_404(
    #     Folder,
    # )
    return render(request, "folder/list_folder.html", {"folders": folders})


def add_folder(request):
    if request.method == "POST":
        form = AddFolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.created_by = request.user
            folder.save()
            messages.success(request, "Folder added successfully")
            return redirect("dashboard")
        else:
            messages.error(request, "Folder not created, try again")
    else:
        form = AddFolderForm()
    return render(request, "folder/add_folder.html", {"form": form})


def edit_folder(request, pk):
    folder = Folder.objects.get(pk=pk)
    # folder = get_object_or_404(Folder, pk=pk)
    if request.method == "POST":
        form = AddFolderForm(request.POST, instance=folder)
        if form.is_valid():
            form.save()

            messages.success(request, "Folder edited successfully")
            return redirect("dashboard")
        else:
            messages.error(request, "Folder not edited, try again")
    else:
        form = AddFolderForm(instance=folder)
    return render(request, "folder/add_folder.html", {"form": form})


def delete_folder(request, pk):
    folder = Folder.objects.get(pk=pk)
    # folder = get_object_or_404(Folder, pk=pk)
    folder.delete()
    return redirect("dashboard")
