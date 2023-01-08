from django.shortcuts import render, redirect

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from creation.forms import CreateTicketAlone, CreateTicketCombine, CreateReview
from website import models


# Create your views here.
class CreationTicketView(LoginRequiredMixin, View):
    template_name = 'creation/ticket_creation.html'
    form_class_creation_ticket = CreateTicketAlone
    
    def get(self, request, *args, **kwargs):
        ticket = models.Ticket.objects.get(id=request.GET['id'])

        ticket_creation = self.form_class_creation_ticket()
        return render(
            request,
            self.template_name,
            context = {
            'form':ticket_creation,
            }
        )
    
    def post(self, request, *args, **kwargs):
        ticket_creation = self.form_class_creation_ticket(request.POST, request.FILES)
        if ticket_creation.is_valid():
            ticket = ticket_creation.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('feed')
        else:
            return render(
                request,
                self.template_name,
                context = {
                    'form':ticket_creation,
                }
            )

class CreationReviewView(LoginRequiredMixin, View):
    template_name = 'creation/review_creation.html'
    form_class_creation_review = CreateReview
    form_class_creation_ticket = CreateTicketCombine

    def get(self, request, *args, **kwargs):
        ticket = models.Ticket.objects.get(id=request.GET['id'])
        
        review_creation = self.form_class_creation_review()
        ticket_creation = self.form_class_creation_ticket(initial={
            'title':ticket.title,
            'description':ticket.description,
            'image':ticket.image,
        })
        return render(
            request,
            self.template_name,
            context = {
                'ticket_form':ticket_creation,
                'review_form':review_creation,
                'ticket_title' : 'Livre / Article',
                'review_title' : 'Critique',
            }
        )

    def post(self, request, *args, **kwargs):
        review_creation = self.form_class_creation_review(request.POST, request.FILES)
        ticket_creation = self.form_class_creation_ticket(request.POST, request.FILES)
        
        if review_creation.is_valid() and ticket_creation.is_valid():
            ticket = ticket_creation.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = review_creation.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('feed')
        else:
            return render(
                request,
                self.template_name,
                context = {
                    'ticket_form':ticket_creation,
                    'review_form':review_creation,
                    'ticket_title' : 'Livre / Article',
                    'review_title' : 'Critique',
                }
            )

class AddReviewView(LoginRequiredMixin, View):
    template_name = 'creation/add_review.html'
    form_class_creation_review = CreateReview
    
    def get(self, request, *args, **kwargs):
        ticket = models.Ticket.objects.get(id=request.GET['id'])
        
        review_creation = self.form_class_creation_review()
        return render(
            request,
            self.template_name,
            context = {
                'title':'nouvelle critique',
                'post':ticket,
                'review_form':review_creation,
                'ticket_title' : 'Livre / Article',
                'review_title' : 'Critique',
            }
        )
    def post():
        pass


