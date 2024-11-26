from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1> sachein is the captain of rcb</h1>')

def vicecaptain(request):
    return HttpResponse('<h1>vijay is thalaivar</h1>')
