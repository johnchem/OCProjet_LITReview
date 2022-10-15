from itertools import chain
from django.shortcuts import render
from django.db.models import CharField, Value
from . import models
from django.contrib.auth.models import User


def feed(request):
    user = User.objects.all().filter(username='paul1')[0]
    print(user)
    tickets = models.Ticket.get_user_followed_tickets(user)
    # returns queryset of tickets
    tickets = tickets.annotable(content_type=Value('TICKET', CharField()))

    reviews = models.Review.get_user_viewable_reviews(user)
    # returns queryset of reviews
    reviews = reviews.annotable(content_type=Value('REVIEW', CharField()))

    #combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )
    return render(request, 'website/feed.html', context={'posts': posts, 'user':user}) 

def main(request):
    return render(request, 'website/main.html')

# Create your views here.
