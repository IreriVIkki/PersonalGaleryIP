from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image, categories

# Create your views here.


def home(request):
    images = Image.all_photos()
    context = {
        'title': 'Galery',
        'images': images,
        'categories': categories
    }
    return render(request, 'home.html', context)


def search_results(request):
    images = Image.all_photos()
    context = {
        'title': 'Galery',
        'images': images,
        'categories': categories
    }
    return render(request, 'search.html', context)
