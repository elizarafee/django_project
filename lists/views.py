from django.shortcuts import render


items = ['a', 'b', 'c']
# Create your views here.
def index(request):
    return render(request, "lists/index.html")

def addItem(request):
    return render(request, "lists/additem.html", {
        "items" : items
    })

def list(request):
    return render(request, "lists/list.html", {
        "items" : items
    })