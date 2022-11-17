from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit, Field, HTML
from django.forms import ModelForm, Textarea, ImageField

from website.models import Ticket, Review

class CreateTicket(ModelForm):
    picture = ImageField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'description',
            HTML("""
            <img id="uploadPreview" src="">
            """),
            Field('image', onchange="PreviewImage()"),
            Submit('Envoyer', 'envoyer')
        )

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
