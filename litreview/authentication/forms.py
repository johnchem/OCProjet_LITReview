from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label="Mot de passe")

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields["username"].widget.attrs.update({
            'class':'form-input',
            'required':'',
            'name':'username',
            'id':'username',
            'type':'text',
            'placeholder':"Nom d'utilisateur",
            'maxlength':'16',
            'minlength':'',
            'help_text':'',
        })
        self.fields["password1"].widget.attrs.update({
            'class':'form-input',
            'required':'',
            'name':'password1',
            'id':'password1',
            'type':'password',
            'placeholder':'password',
            'maxlength':'22',
            'minlength':'8',
            'help_text':'',
        })
        self.fields["password2"].widget.attrs.update({
            'class':'form-input',
            'required':'',
            'name':'password2',
            'id':'password2',
            'type':'password',
            'placeholder':'password',
            'maxlength':'22',
            'minlength':'8',
            'help_text':'',
        }) 
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2')

def CustomSignUpForm(UserCreationForm):
    username=forms.CharField(label='username', nim_length=5, max_length=150)
    password1=forms.CharField(label='password', widget=forms.PasswordInput) 
    password2=forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def username_clean(self):
        username=self.cleaned_data['username'].lower()
        new=User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2

    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user