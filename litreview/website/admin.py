from django.contrib import admin
from .models import UserFollows, Ticket, Review

admin.site.register(UserFollows)
admin.site.register(Ticket)
admin.site.register(Review)
