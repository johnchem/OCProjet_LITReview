from itertools import chain

from django.views import View
from django.db.models import Value, CharField
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from creation.forms import CreateTicketAlone, CreateTicketCombine, CreateReview
from website import models


# Create your views here.
class creationTicketView(LoginRequiredMixin, View):
    template_name = 'creation/ticket_creation.html'
    form_class_creation_ticket = CreateTicketAlone
    
    def get(self, request, *args, **kwargs):
        ticket_creation = self.form_class_creation_ticket()

        return render(
            request,
            self.template_name,
            context = {
            'title': 'Créer un ticket',
            'form':ticket_creation,
            }
        )
    
    def post(self, request, *args, **kwargs):
        ticket_creation = self.form_class_creation_ticket(request.POST, request.FILES)
        if ticket_creation.is_valid():
            ticket = ticket_creation.save(commit = False)
            ticket.user = request.user
            ticket.save()
            return redirect('feed')
        else:
            return render(
                request,
                self.template_name,
                context = {
                    'title': 'Créer un ticket',
                    'form':ticket_creation,
                }
            )


class updateTicketView(LoginRequiredMixin, View):
    template_name = 'creation/ticket_creation.html'
    form_class_creation_ticket = CreateTicketAlone
    
    def get(self, request, *args, **kwargs):
        ticket = models.Ticket.objects.get(id=request.GET['ticket_id'])
        ticket_creation = self.form_class_creation_ticket(instance=ticket)

        return render(
            request,
            self.template_name,
            context = {
            'title': 'modifier un ticket',
            'form':ticket_creation,
            }
        )
    
    def post(self, request, *args, **kwargs):
        ticket = models.Ticket.objects.get(id=request.GET['ticket_id'])
        ticket_creation = self.form_class_creation_ticket(
            request.POST, 
            request.FILES, 
            instance=ticket
            )
        if ticket_creation.is_valid():
            ticket_creation.user = request.user
            ticket_creation.save()
            return redirect('user_posts', username=request.user)
        else:
            return render(
                request,
                self.template_name,
                context = {
                    'title': "Modification d'un ticket",
                    'form':ticket_creation,
                }
            )


class creationReviewView(LoginRequiredMixin, View):
    template_name = 'creation/review_creation.html'
    form_class_creation_review = CreateReview
    form_class_creation_ticket = CreateTicketCombine

    def post(self, request, *args, **kwargs):
        review_creation = self.form_class_creation_review(request.POST, request.FILES)
        ticket_creation = self.form_class_creation_ticket(request.POST)
        
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
                    'title': 'Créer un ticket et une revue',
                    'ticket_form':ticket_creation,
                    'review_form':review_creation,
                    'ticket_title' : 'Livre / Article',
                    'review_title' : 'Critique',
                }
            )


class addReviewView(LoginRequiredMixin, View):
    template_name = 'creation/add_review.html'
    form_class_creation_review = CreateReview
    
    def get(self, request, *args, **kwargs):
        ticket = models.Ticket.objects.get(id=request.GET['ticket_id'])
        review_creation = self.form_class_creation_review()
        title = "création d'une nouvelle revue"

        return render(
                request,
                self.template_name,
                context = {
                    'title': title,
                    'post':ticket,
                    'review_form': review_creation,
                    'ticket_title' : 'Livre / Article',
                    'review_title' : 'Critique',
                }
            )

    def post(self, request, *args, **kwargs):
        ticket = models.Ticket.objects.get(id=request.POST['ticket_id'])
        form = self.form_class_creation_review(request.POST)
        
        if form.is_valid():
            form = form.save(commit = False)
            form.ticket = ticket
            form.user = request.user
            form.save()
        return redirect('feed')


class updateReviewView(LoginRequiredMixin, View):
    template_name = 'creation/review_creation.html'
    form_class_creation_review = CreateReview
    form_class_creation_ticket = CreateTicketCombine

    def post(self, request, *args, **kwargs):
        review = models.Review.objects.get(id=request.GET['review_id'])
        ticket = review.ticket

        review_creation = self.form_class_creation_review(instance=review)
        title = "Modification de la revue"

        return render(
                request,
                self.template_name,
                context = {
                    'title': title,
                    'post':ticket,
                    'review_form': review_creation,
                    'ticket_title' : 'Livre / Article',
                    'review_title' : 'Critique',
                }
            )

    def post(self, request, *args, **kwargs):
        review = models.Review.objects.get(id=request.GET['review_id'])
        ticket = review.ticket
        
        review_update = self.form_class_creation_review(
            request.POST, 
            request.FILES,
            instance=review
            )
        title="Modification de la revue"
        
        if review_update.is_valid():
            review_update.save()
            return redirect('user_posts', username=request.user)
        else:
            return render(
                request,
                self.template_name,
                context = {
                    'title': title,
                    'post':ticket,
                    'review_form': review_update,
                    'ticket_title' : 'Livre / Article',
                    'review_title' : 'Critique',
                }
            )
        
class userPostHistory(LoginRequiredMixin, View):
    template_name = "creation/user_posts.html"
    
    def post(self, request, *args, **kwargs):
        user = request.user
        user_tickets = models.Ticket.objects.filter(user=user)
        user_tickets = user_tickets.annotate(content_type=Value('TICKET', CharField()))

        user_reviews = models.Review.objects.filter(user=user)
        user_reviews = user_reviews.annotate(content_type=Value('REVIEW', CharField()))

        posts = sorted(
            chain(user_reviews, user_tickets),
            key= lambda posts: posts.time_created,
            reverse=True
        )

        return render(request, 
            self.template_name,
            context = {
                'posts':posts,
                'title':'Vos posts',
                'user_feed':True,
            }
        )

    def get(self, request, *args, **kwargs):
        user = request.user
        user_tickets = models.Ticket.objects.filter(user=user)
        user_tickets = user_tickets.annotate(content_type=Value('TICKET', CharField()))

        user_reviews = models.Review.objects.filter(user=user)
        user_reviews = user_reviews.annotate(content_type=Value('REVIEW', CharField()))

        posts = sorted(
            chain(user_reviews, user_tickets),
            key= lambda posts: posts.time_created,
            reverse=True
        )

        return render(request, 
            self.template_name,
            context = {
                'posts':posts,
                'title':'Vos posts',
                'user_feed':True,
            }
        )
