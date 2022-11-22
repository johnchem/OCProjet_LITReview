from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit, Field, HTML, Div
from django import forms

from website.models import Ticket, Review

class TicketLayout(Layout):
    def __init__(self, *args, **kwargs):
        super().__init__(
            Field('title', placeholder="Titre"),
            Field('description', placeholder="Taper votre message ici"),
            HTML("""
            <img id="uploadPreview" src="">
            """),
            Field('image', onchange="PreviewImage()"),
        )

class ReviewLayout(Layout):
    rating = forms.ChoiceField(widget=forms.RadioSelect)
    def __init__(self, *args, **kwargs):
        super().__init__(
            Field('headline', placeholder='Titre'),
            'rating',
            Field('body', placeholder='Commentaire'),
        )

class CreateTicket(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateTicket, self).__init__(*args, **kwargs)
        self.fields['title'].label = ''
        self.fields['description'].label = ''
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            TicketLayout(),
            Submit('Envoyer', 'envoyer')
        )

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

class CreateReview(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(CreateReview, self).__init__(*args, **kwargs)
        self.fields['title'].label = ''
        self.fields['Description'].label = ''
        self.fields['headline'].lable = ''
        self.fields['body'].label = ''

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                HTML("""
                <p>{{ticket_title}}</p>
                """, css_class= "title review__creation__title"),
                TicketLayout(),
            ),
            Div(
                HTML("""
                <p>{{review_title}}</p>
                """, css_class = "title review__creation__title"),
                ReviewLayout(),
                Submit('Envoyer', 'envoyer')
            )
        )
    class Meta:
        model = [Ticket, Review]
        fields = ['title', 'description', 'image', 'headline', 'rating', 'body']