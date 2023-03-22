from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from django.forms import ModelForm
from django import forms

from website.models import UserFollows


class SearchBox(forms.Form):
    username = forms.CharField(
        label='',
        max_length=63
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'placeholder': 'Suivre un utilisateur'
        })

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_id = 'search__user__form'
        helper.form_method = 'POST'
        helper.add_input(Submit(
            name="search__button",
            value="Envoyer",
            css_class="search__button button"
            ))
        return helper


class FollowedUserForm(ModelForm):
    user = forms.CharField(
        label='',
        widget=forms.HiddenInput,
        )

    followed_user = forms.CharField(
        label='',
        widget=forms.HiddenInput(attrs={
            'label': 'followed_user',
            }
            )
        )

    class Meta:
        model = UserFollows
        fields = ['user', 'followed_user', ]


class FollowedUserFormSetHelper(FormHelper):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.form_method = 'post'
        self.layout = Layout(
            Fieldset(
                'user',
                'followed_user',
            ),
            Submit(
                name='unfollow__button',
                value='Se désabonner',
                css_class='unfollow__button',
            )
        )
