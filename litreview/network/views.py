from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import get_object_or_404

from . import forms
from website import models


class UserNetwork(LoginRequiredMixin, View):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name='network/subscription.html'
    form_class = forms.SearchBox

    
    def get(self, request, **kwargs):
        searchbox_form = self.form_class()
        subscrip_form = ""
        user = request.user

        followers = models.UserFollows.objects.filter(user__in=user)

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
            )