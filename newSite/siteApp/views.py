from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hello muzafaka')
def home(request):
    return HttpResponse('dddddd')