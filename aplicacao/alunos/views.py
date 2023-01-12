from django.shortcuts import render
from django.http import Httpresponse

# Create your views here.
def index(request):
    return Httpresponse('<h1>Larissa</h1>')