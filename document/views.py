from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import AddDocumentForm
from .models import Document

# Create your views here.


@login_required(login_url="/")
def list_document(request):
    form = AddDocumentForm()
    if request.user.is_staff:
        documents = Document.objects.all()
    else:
        documents = Document.objects.filter(created_by=request.user)
    context = {
        "documents": documents,
        "form":form
    }
    return render(request, "document/list_document.html", context)


@login_required(login_url="/")
def add_document(request):
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
        form = AddDocumentForm()
    return render(request, "document/add_document.html", {"form": form})


@login_required(login_url="/")
def edit_document(request, pk):
    document = Document.objects.get(created_by=request.user, pk=pk)
    if request.method == "POST":
        form = AddDocumentForm(
            request.POST or None, request.FILES or None, instance=document
        )
        if form.is_valid():
            form.save()

            messages.success(request, "document edited successfully")
            return redirect("dashboard")
        else:
            messages.error(request, "document not edited, try again")
    else:
        form = AddDocumentForm(instance=document)
    return render(request, "document/add_document.html", {"form": form})


@login_required(login_url="/")
def detail_document(request, pk):
    document = Document.objects.get(created_by=request.user, pk=pk)
    return render(request, "document/detail_document.html", {"document": document})


@login_required(login_url="/")
def delete_document(request, pk):
    document = Document.objects.get(created_by=request.user, pk=pk)
    document.delete()
    return redirect("list_document")
