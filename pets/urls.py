from django.urls import path
from . import views


app_name = "pets"
urlpatterns = [
    path("", views.index, name= "index"),
    path("<str:petname>", views.pet, name="pet"),
]

