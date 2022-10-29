from logging import PlaceHolder
from tkinter import Widget
from turtle import width
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label="Mot de passe")

class CustomSignUpForm(forms.Form):
    username = forms.CharField(label='username')
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput)
    class Meta(forms.Form):
        model=User
        field=('username', 'password1', 'password2')
    

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].label = ''
        
        self.fields["username"].widget.attrs.update({
            'class':'form-input',
            'required':'True',
            'name':'username',
            'type':'text',
            'placeholder':"Nom d'utilisateur",
        })
        self.fields["password1"].widget.attrs.update({
            'class':'form-input',
            'required':'True',
            'name':'password1',
            'type':'password',
            'placeholder':'Mot de passe',
            'maxlength':16,
        })
        self.fields["password2"].widget.attrs.update({
            'class':'form-input',
            'required':'True',
            'name':'password2',
            'type':'password',
            'placeholder':'Confirmer mot de passe',
            'maxlenght':16,
        })
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2')