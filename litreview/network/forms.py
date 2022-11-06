
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django import forms


class SearchBox(forms.Form):
    username = forms.CharField(
        label='',
        max_length=63
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update[{
            'placeholder':'Suivre un utilisateur'
        }]

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