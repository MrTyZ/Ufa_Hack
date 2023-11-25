from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
User=get_user_model()

class Subject(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image = models.ImageField()
    def __str__(self) -> str:
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500) 
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT, null=False)

    def __str__(self) -> str:
        return self.title
    

class Question_Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class Question(models.Model):
    text = models.CharField(max_length=255)
    type =  models.ForeignKey('Question_Type', on_delete=models.PROTECT, null=True)
    
    def __str__(self) -> str:
        return self.text
    

class Choice(models.Model):
    text = models.CharField(max_length=100) 
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=False)
    is_correct = models.BooleanField()

    def __str__(self) -> str:
        return self.text



class UserProgress(models.Model):

    course = models.ForeignKey('Course', on_delete=models.PROTECT, null=False)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=False)
    #user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num = models.IntegerField()


    def __str__(self) -> str:
        return self.course.title
