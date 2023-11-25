from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from shop.models import Subject, Choice, Course, Question, Question_Type
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
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy



class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    """def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = 
        return dict(list(context.items()) + list(c_def.items()))
"""

def courses(request, subject_id):
    course=Course.objects.all()
    return render(request, "Courses.html",{'courses': Course.objects.all().filter(subject_id=subject_id)})

def test(request,course_id):
    if 'correct_list' not in request.session:
        request.session['correct_list'] = []
    
    	
    
    question_num = request.session.get('q', 0)
    questions_list = Question.objects.all()

    request.session.get('correct_list', [0,])

    if Choice.objects.get(pk=request.POST.get("test")).is_correct:
          
        corr_item = Question.objects.all()[question_num-1: question_num].values('id')[0]
        corr_id = corr_item['id']
        request.session['correct_list'].append(corr_id)
        #request.session['correct_list'].append(Question.objects.all()[question_num-1: question_num].id)
        print(request.session['correct_list'])

    if question_num >= questions_list.count():
        question_num = 0
        return render(request, "results.html", {"questions": Question.objects.all(), "choices": Choice.objects.all(), "correct_list": request.session['correct_list']} )

    quest_lst = questions_list[ question_num: question_num+1]
    
    request.session['q'] =  question_num + 1

    return render(request, "test.html", {'questions': quest_lst, 'choices': Choice.objects.all()} )



def index(request): 
    return render(request, 'index.html', {'subjects': Subject.objects.all(), 'courses': Course.objects.all()})


"""def test(request):
    return render(request, 'test.html')"""

def items_app(request): 
    return render(request, 'main_app.html')

"""class ItemView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer"""

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
    #return HttpResponse(jsondata, content_type="application/json")
    
    return res


def subj1(request):
   
    return JsonResponse({'title':'kek'})




class SubjectAPIList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectsSerializer
    def get(self, request):
        lst = Subject.objects.all()
        return Response({'subjects':  SubjectsSerializer(lst, many = True).data})
    #permission_classes = (IsAuthenticatedOrReadOnly,)

"""class ItemAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)
  
class ItemAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer  
    permission_classes = (IsAdminOrReadOnly,)
"""

"""class ItemViewSet(viewsets.ModelViewSet):
    #queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Item.objects.all()[:3]
        
        return Item.objects.filter(pk=pk)

    @action(methods=['get'], detail = True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})"""

"""class ItemAPIList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemAPIUpdate(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer"""

'''class ItemView(APIView):
    queryset = Item.objects.all()

    def get(self, request):
        lst = Item.objects.all()
        return Response({'items':  ItemSerializer(lst, many = True).data})
    
    def post(self, request):
        """category = Category.objects.get(pk=request.data['category'])
        request.data['category'] = category"""
        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        """item_new = Item.objects.create(
            name=request.data['name'],
            description = request.data['description'],
            price = request.data['price'],
            category = Category.objects.get(id=request.data['category'])
        )
        return Response({'item': model_to_dict(item_new)})"""
        return Response({'item': serializer.data})
    

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed" })
        
        try:
            instance = Item.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist" })
        
        serializer = ItemSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'item': serializer.data})


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method DELETE not allowed" })
        
        try:
            Item.objects.get(pk=pk).delete()
        except:
            return Response({"error": "Object does not exist" })
        


        return Response({'item': "delete item: " + str(pk)})'''
        

    

    


