from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label= 'login', widget= forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label= 'pass1', widget= forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label= 'pass2', widget= forms.PasswordInput(attrs={'class':'form-input'}))
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
        widgets = {'username': forms.TextInput(attrs={'class':'form-input'}),
                   'password1': forms.PasswordInput(attrs={'class':'form-input'}),
                   'password2': forms.PasswordInput(attrs={'class':'form-input'})}