from itertools import chain
from pyexpat import model
from django.shortcuts import render
from django.db.models import CharField, Value
from . import models
from django.contrib.auth.models import User


def feed(request):
    user = User.objects.all().filter(username='paul1')[0]
    followed_user = [x.followed_user.id for x in models.UserFollows.objects.filter(user=user)]

    tickets = models.Ticket.objects.filter(user__in=followed_user)
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    reviews = models.Review.objects.filter(user__in=followed_user)
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    #combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )
    print([x.content_type for x in posts])
    return render(request, 'website/feed.html', context={'posts': posts, 'user': user}) 

def main(request):
    return render(request, 'website/main.html')

# Create your views here.
