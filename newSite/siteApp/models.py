from django.db import models

<<<<<<< HEAD
class Subject(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500) 
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT, null=False)


class Question_Type(models.Model):
    name = models.CharField(max_length=100)


class Question(models.Model):
    text = models.CharField(max_length=255)
    type =  models.ForeignKey('Question_Type', on_delete=models.PROTECT, null=True)

class Choice(models.Model):
    text = models.CharField(max_length=100) 
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=False)
    is_correct = models.BooleanField()
=======
class Test(models.Model):
    title=models.CharField(max_length=255)
>>>>>>> e9217f1bebee03a0951a0ad91eae454b6d07e14b
