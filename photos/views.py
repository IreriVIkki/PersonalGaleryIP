from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def home(request):
    context = {
        'title': 'Galery'
    }

    # a retun value must have a get method to it
    return render(request, 'home.html', context)
