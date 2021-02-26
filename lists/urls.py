from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("additem", views.addItem, name = "additem"),   #dynamic url uses the  value of the name attribute to determine the path
    path("list", views.list, name = "list")
]
