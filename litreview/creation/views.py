from django.shortcuts import render, redirect

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from creation.forms import CreateTicket, CreateReview



# Create your views here.
class CreationTicketView(LoginRequiredMixin, View):
    template_name = 'creation/ticket_creation.html'
    form_class_creation_ticket = CreateTicket

    def get(self, request, *args, **kwargs):
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

    def get(self, request, *args, **kwargs):
        review_creation = self.form_class_creation_review()
        return render(
            request,
            self.template_name,
            context = {
                'form':review_creation,
                'ticket_title' : 'Livre / Article',
                'review_title' : 'Critique',
            }
        )

    def post(self, request, *args, **kwargs):
        review_creation = self.form_class_creation_review(request.POST, request.FILES)
        if review_creation.is_valid():
            review = review_creation.save(commit=False)
            review.user = request.user
            # review.save()
            return redirect('feed')
        else:
            return render(
                request,
                self.template_name,
                context = {
                    'form':review_creation,
                    'ticket_title' : 'Livre / Article',
                    'review_title' : 'Critique',
                }
            )
    