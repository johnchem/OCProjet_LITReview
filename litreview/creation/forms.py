from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm

from website.models import Ticket, Review

class CreateTicket(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.append(Submit('Envoyer', 'envoyer'))

    class Meta:
        model = Ticket
        fields=['title, description', 'image', ]
