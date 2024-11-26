from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1> Ruthraj is the captain of csk</h1>')

def vicecaptain(request):
    return HttpResponse('<h1>Dhoni is thalaivar</h1>')
