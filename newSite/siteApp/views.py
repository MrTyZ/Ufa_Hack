from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Subject


# Create your views here.
def index(request):
    return HttpResponse('hello muzafaka')
def home(request):
    return HttpResponse('dddddd')



class SubjectListAPI(APIView):
    def get(self, request):
        queryset = Subject.objects.all()