from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

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

