
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import modelformset_factory

from django import forms


class SearchBox(forms.Form):
    username = forms.CharField(
        label='',
        max_length=63
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'placeholder':'Suivre un utilisateur'
        })

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_id = 'search__user__form'
        helper.form_method = 'GET'
        helper.add_input(Submit(
            name="search__button",
            value="Suivre Utilisateur",
            css_class="search__button button"
            ))
        return helper

class FollowedUserForm(forms.Form):
    login_user = None
    user = None
    follow = forms.BooleanField(
        initial=True,
        )
    
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    @property
    def helper(self, login_user, user):
        helper = FormHelper()
        helper.add_input(Submit(
            name=f'search__button {self.user.username}',
            value='Se désabonner',
            css_class='unfollow__button', 
        ))