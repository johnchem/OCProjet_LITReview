from itertools import chain

from django.shortcuts import render
from django.db.models import CharField, Value, Case, When, BooleanField, Q
from django.contrib.auth.models import User

from . import models

def feed(request):
    user = User.objects.all().filter(username='paul1')[0]
    followed_user = [x.followed_user.id for x in models.UserFollows.objects.filter(user=user)]
    reviewed_ticket = [x.id for x in models.Ticket.objects.filter(review__user=user)]

    tickets = models.Ticket.objects.filter(Q(user__in=followed_user)|Q(user=user))
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()),
                               user_reviewed_ticket=Case(
                                When(id__in=reviewed_ticket, then=Value(True, BooleanField())),
                                default=Value(False, BooleanField()))                   
                                )

    reviews = models.Review.objects.filter(Q(user__in=followed_user)|Q(user=user))
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()),
                               user_reviewed_ticket=Case(
                                When(ticket__in=reviewed_ticket, then=Value(True, BooleanField())),
                                default=Value(False, BooleanField()))                   
                                )

    review_user_ticket = models.Review.objects.filter(ticket__user=user).exclude(Q(user__in=followed_user)|Q(user=user))
    # returns queryset of user's reviews
    review_user_ticket = review_user_ticket.annotate(
                            content_type=Value('REVIEW', CharField()),
                            user_reviewed_ticket=Case(
                                When(ticket__in=reviewed_ticket, then=Value(True, BooleanField())),
                                default=Value(False, BooleanField())
                            )
                        )
    
    #combine and sort the two types of posts
    posts = sorted(
        chain(reviews, review_user_ticket, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )
    print([x.user_reviewed_ticket for x in posts])
    return render(request, 'website/feed.html', context={'posts': posts, 'user': user}) 

def main(request):
    return render(request, 'website/main.html')

# Create your views here.
