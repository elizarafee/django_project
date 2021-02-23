from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Welcome to Pets App')

def pet(request, petname):
    return render(request, 'pets/pet.html', {
        "petname": petname
    })