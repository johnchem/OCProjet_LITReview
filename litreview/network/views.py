from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory

from . import forms
from website import models


class UserNetwork(LoginRequiredMixin, View):
    template_name='network/subscription.html'
    form_class_search_box = forms.SearchBox
    form_class_followed_user = forms.FollowedUserForm

    
    def get(self, request, **kwargs):
        searchbox_form = self.form_class_search_box()
        
        user = request.user
        followed_user = [x.followed_user for x in models.UserFollows.objects.filter(user=user)]
        FollowedUserSet = modelformset_factory(
            models.UserFollows,
            form = self.form_class_followed_user,
            fields = ("followed_user", ), 
            )
        formset = FollowedUserSet()

        followers = [x.user.username for x in models.UserFollows.objects.filter(followed_user=user)]

        return render(
            request,
            self.template_name,
            context={
                "name":"Abonnement",
                "searchbox_form": searchbox_form,
                "subscrip_form": formset,
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