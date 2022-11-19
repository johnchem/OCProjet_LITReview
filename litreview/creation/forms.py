from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit, Field, HTML
from django.forms import ModelForm, Textarea, ImageField

from website.models import Ticket, Review

class CreateTicket(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateTicket, self).__init__(*args, **kwargs)
        self.fields['title'].label = ''
        self.fields['description'].label = ''
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title', placeholder="Titre"),
            Field('description', placeholder="Taper votre message ici"),
            HTML("""
            <img id="uploadPreview" src="">
            """),
            Field('image', onchange="PreviewImage()"),
            Submit('Envoyer', 'envoyer')
        )

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

