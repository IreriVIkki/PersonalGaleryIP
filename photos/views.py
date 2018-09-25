from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):


    # a retun value must have a get method to it
    return HttpResponse('asdf')
