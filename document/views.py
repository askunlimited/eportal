from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import AddDocumentForm
from .models import Document

# Create your views here.


@login_required
def list_document(request):
    documents = Document.objects.filter(created_by=request.user)
    return render(request, "document/list_document.html", {"documents": documents})


@login_required(login_url="/")
def add_document(request):
    if request.method == "POST":
        form = AddDocumentForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.created_by = request.user
            document.save()
            messages.success(request, "document added successfully")
            return redirect("dashboard")
        else:
            messages.error(request, "document not created, try again")
    else:
        form = AddDocumentForm()
    return render(request, "document/add_document.html", {"form": form})


@login_required(login_url="/")
def edit_document(request, pk):
    document = Document.objects.get(created_by=request.user, pk=pk)
    if request.method == "POST":
        form = AddDocumentForm(request.POST, instance=document)
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



def delete_document(request, pk):
    document = Document.objects.get(created_by=request.user, pk=pk)
    document.delete()
    return redirect("list_document")
