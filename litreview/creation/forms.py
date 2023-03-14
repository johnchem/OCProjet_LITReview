from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit, Field, HTML, Div
from django import forms

from website.models import Ticket, Review

class TicketLayout(Layout):
    def __init__(self, *args, **kwargs):
        super().__init__(
            Field('title', placeholder="Titre"),
            Field('description', placeholder="Taper votre message ici"),
            Field('image', 
                  onchange="PreviewImage()", 
                  css_class="button",
                  ),
            HTML("""
            <img id="uploadPreview" src="">"""),
        )

class ReviewLayout(Layout):
    rating = forms.ChoiceField(widget=forms.RadioSelect)
    def __init__(self, *args, **kwargs): 
        super().__init__(
            Field('headline', placeholder='Titre'),
            'rating',
            Field('body', placeholder="Taper votre message ici"),
        )

class CreateTicketAlone(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateTicketAlone, self).__init__(*args, **kwargs)
        self.fields['title'].label = ''
        self.fields['description'].label = ''

        self.fields['image'].label = 'Image'
        self.fields['image'].widget.label = 'Nouvelle'
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            TicketLayout(),
            Submit('envoyer','Envoyer', 
                   css_class="button",
                   )
        )

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

class CreateTicketCombine(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateTicketCombine, self).__init__(*args, **kwargs)
        self.fields['title'].label = ''
        self.fields['description'].label = ''

        self.fields['image'].label = 'Couverture'
        self.fields['image'].attrs = {'class' : 'image_container'} # effet ? 
        self.fields['image'].widget.initial_text = 'Actuel'
        self.fields['image'].widget.input_text = 'Nouvelle'
        # self.fields['image'].widget.attrs = {'class':'turlututu'}
        
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TicketLayout()
        )

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

class CreateReview(forms.ModelForm):
    CHOICES = [('0','- 0'),
                   ('1','- 1'),
                   ('2','- 2'),
                   ('3','- 3'),
                   ('4','- 4'),
                   ('5','- 5'),
        ]
    rating = forms.ChoiceField(choices=CHOICES,
                            widget=forms.RadioSelect
                            )
    def __init__(self,*args, **kwargs):
        super(CreateReview, self).__init__(*args, **kwargs)
        self.fields['headline'].label = 'Titre'
        self.fields['body'].label = 'Commentaire'
        self.fields['rating'].label = 'Note'

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            ReviewLayout(),
        )
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']