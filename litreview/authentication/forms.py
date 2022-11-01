from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model



class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)
    
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].label = ''
        
        self.fields["username"].widget.attrs.update({
            'placeholder':"Nom d'utilisateur",
        })
        self.fields["password"].widget.attrs.update({
            'placeholder':'Mot de passe',
            'maxlength':16,
        })



class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.helper = FormHelper()
        self.helper.form_id = 'signup__form'
        self.helper.form_method = 'post'
        self.helper.error_text_inline = False
        
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