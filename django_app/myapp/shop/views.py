from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from shop.models import Subject, Choice, Course, Question, UserProgress
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from shop.serializers import SubjectsSerializer
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from django.core import serializers
import json
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from .forms import RegisterUserForm
from django.contrib.auth.views import LoginView


def index(request): 
    return render(request, 'index.html', {'subjects': Subject.objects.all(), 'courses': Course.objects.all()})



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    
class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse_lazy('index')



def courses(request, subject_id):
    course=Course.objects.all()
    request.session['q'] = 0
    request.session['correct_list'] = []
    return render(request, "Courses.html",{'courses': Course.objects.all().filter(subject_id=subject_id)})

def test(request,course_id):
    if 'correct_list' not in request.session:
        request.session['correct_list'] = []
    
    question_num = request.session.get('q', 0)
    questions_list = Question.objects.all()

    request.session.get('correct_list', [0,])
    if request.method == "POST" and question_num != 0:
        if Choice.objects.get(pk=request.POST.get("test")).is_correct:
            
            corr_item = Question.objects.all()[question_num-1: question_num].values('id')[0]
            corr_id = corr_item['id']
            request.session['correct_list'].append(corr_id)
            print(request.session['correct_list'])

    print(questions_list)
    print(question_num)
    if question_num >= questions_list.count():
        question_num = 0
        request.session['q'] = 0
        #UserProgress.objects.create(course=Course.objects.get(pk=course_id), user=User.request.user.id, num=5)
        return render(request, "results.html", {"questions": Question.objects.all(), "choices": Choice.objects.all(), "correct_list": request.session['correct_list']} )

    quest_lst = questions_list[ question_num: question_num+1]
    
    request.session['q'] =  question_num + 1

    return render(request, "test.html", {'questions': quest_lst, 'choices': Choice.objects.all()} )



def items_app(request): 
    return render(request, 'main_app.html')


def subj(request):
    
    data = Subject.objects.all()
    res= JsonResponse({"name": "Tom", "age": 38})
    res["Access-Control-Allow-Origin"]="*"
    res["Access-Control-Allow-Methods"]="GET"
    res["Access-Control-Max-Age"] = "1000"
    res["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    jsondata = serializers.serialize('json', data)
    """f request.method == "GET":
        data = {
            "asd": 123
        }
        resp = json.dump(data)
        return HttpResponse(json.dumps(data), mimetype ="application/json")"""
    return res




class SubjectAPIList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectsSerializer
    def get(self, request):
        lst = Subject.objects.all()
        return Response({'subjects':  SubjectsSerializer(lst, many = True).data})
    #permission_classes = (IsAuthenticatedOrReadOnly,)


    


