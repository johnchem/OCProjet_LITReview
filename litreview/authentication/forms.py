from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        max_length=63)
    password = forms.CharField(
        max_length=63,
        widget=forms.PasswordInput)

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        for field in self.fields:
            self.fields[field].label = ''

        self.fields["username"].widget.attrs.update({
            'placeholder': "Nom d'utilisateur",
        })
        self.fields["password"].widget.attrs.update({
            'placeholder': 'Mot de passe',
            'maxlength': 16,
        })

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_id = 'login__form'
        helper.form_method = 'POST'
        helper.form_show_errors = True
        helper.error_text_inline = True
        # self.helper.add_input(Submit("login__button","Se Connecter"))
        helper.add_input(Submit(name="login__button",
                                value="Se Connecter",
                                css_class="login__button button"))
        return helper


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].label = ''

        self.fields["username"].widget.attrs.update({
            'class': 'form-input',
            'required': 'True',
            'name': 'username',
            'type': 'text',
            'placeholder': "Nom d'utilisateur",
        })
        self.fields["password1"].widget.attrs.update({
            'class': 'form-input',
            'required': 'True',
            'name': 'password1',
            'type': 'password',
            'placeholder': 'Mot de passe',
            'maxlength': 16,
        })
        self.fields["password2"].widget.attrs.update({
            'class': 'form-input',
            'required': 'True',
            'name': 'password2',
            'type': 'password',
            'placeholder': 'Confirmer mot de passe',
            'maxlenght': 16,
        })

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_id = 'signup__form'
        helper.form_method = 'post'
        helper.error_text_inline = False
        return helper

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2')
