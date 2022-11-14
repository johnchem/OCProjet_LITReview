from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from django.forms import ModelForm

from website.models import Ticket, Review

class CreateTicket(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_layout(HTML(
            """{% if form.image.value %}
            <img class='create__ticket__picture' 
            src='{{ MEDIA_URL }}{{ form.image.value }}'>
            {% endif %}"""
            ))
        self.helper.add_input(Submit('Envoyer', 'envoyer'))

    class Meta:
        model = Ticket
        fields = ('title', 'description', 'image')
