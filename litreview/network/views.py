from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import get_object_or_404
from django.forms import formset_factory

from . import forms
from website import models


class UserNetwork(LoginRequiredMixin, View):
    model = User
    template_name='network/subscription.html'
    form_class = forms.SearchBox

    
    def get(self, request, **kwargs):
        searchbox_form = self.form_class()
        subscrip_form = ""
        user = request.user

        followers = [x.user.username for x in models.UserFollows.objects.filter(followed_user=user)]

        return render(
            request,
            self.template_name,
            context={
                "name":"Abonnement",
                "searchbox_form": searchbox_form,
                "subscrip_form": subscrip_form,
                "followers": followers,
            }
        )

    def post(self, request, **kwargs):
        form = self.form_class()
        
        return render(
            request,
            self.template_name,
            context={
                "name":"Abonnement",
            }
        )

class FollowUser(LoginRequiredMixin, View):
    template_name = 'network/userfollewed.html'
    form_class = forms.FollowedUserForm

    def get(self, request):
        user = request.user
        followed_user = [x.followed_user for x in models.UserFollows.objects.filter(user=user)]
        FollowedUserSet = formset_factory(self.form_class, extra=len(followed_user))
        formset = FollowedUserSet()

        return render(
            request, 
            self.template_name,
            context={
                'formset':formset
            }
            )

        