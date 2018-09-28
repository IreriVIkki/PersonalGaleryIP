from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image, categories

# Create your views here.


def home(request):
    images = Image.all_photos()
    caption = 'Beautiful Photo Galery'
    message = 'A collection of the best photos taken by various incredible photographers from all over the world'
    context = {
        'title': 'Galery',
        'caption': caption,
        'message': message,
        'images': images,
        'categories': categories
    }
    return render(request, 'home.html', context)


def search_results(request):
    # check if the input field exists and that ic contains data
    if 'image' in request.GET and request.GET['image']:
        # get the data from the search input field
        search_term = request.GET.get('image')
        searched_images = Image.filter_by_search_term(search_term)
        caption = f'{search_term}'
        search_context = {
            'title': 'Galery',
            'images': searched_images,
            'caption': caption,
            'message': '',
            'categories': categories
        }
        return render(request, 'search.html', search_context)
    else:
        images = Image.all_photos()
        search_context = {
            'title': 'Galery',
            'images': searched_images,
            'message': '',
            'caption': 'No Results Found',
            'categories': categories
        }
        return render(request, 'search.html', search_context)

    images = Image.all_photos()
    context = {
        'title': 'Galery',
        'images': images,
        'categories': categories
    }
    return render(request, 'search.html', context)
