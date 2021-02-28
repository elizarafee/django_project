from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class addingItemForm(forms.Form):
    itemName = forms.CharField(label="Item Name")
    # priorirty = forms.IntegerField(label="Priority", min_value=3, max_value=6)

items = []

# Create your views here.
def index(request):
    return render(request, "lists/index.html")

def list(request):
    return render(request, "lists/list.html", {
        "items" : items
    })

def addItem(request):
    if request.method == "POST":
        form = addingItemForm(request.POST)
        if form.is_valid():
            itemName = form.cleaned_data["itemName"]
            items.append(itemName)
            return HttpResponseRedirect(reverse("lists:list"))
        else:
            print("form")
            return render(request, "lists/addItem.html", {
            "form": form
            })
    
    return render(request, "lists/addItem.html", {
        "form": addingItemForm()
    })