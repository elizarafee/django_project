from django.urls import path
from . import views


app_name = "lists"
urlpatterns = [
    path("", views.index, name = "index"),
    path("additem", views.addItem, name = "additem"),   
    path("list", views.list, name = "list")
]
