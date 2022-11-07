from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory

from . import forms
from website import models
from network.forms import FollowedUserFormSetHelper


class UserNetwork(LoginRequiredMixin, View):
    template_name='network/subscription.html'
    form_class_search_box = forms.SearchBox
    form_class_followed_user = forms.FollowedUserForm

    
    def get(self, request, **kwargs):
        searchbox_form = self.form_class_search_box()
        
        user = request.user
        followed_users = [x.followed_user for x in models.UserFollows.objects.filter(user=user)]
        print(*followed_users)
        FollowedUserSet = modelformset_factory(
            models.UserFollows,
            form = self.form_class_followed_user,
            extra=3, 
            )
        
        data = []
        for followed_user in followed_users:
            data.append({
                'user':user.username,
                'followed_user':followed_user.username})

        formset = FollowedUserSet(initial=data,)
        helper = FollowedUserFormSetHelper()
        # helper.add_input(Submit(
        #     name='unfollow__button',
        #     value='Se désabonner',
        #     css_class='unfollow__button',
        #     ))
        # formset = self.form_class_followed_user()

        followers = [x.user.username for x in models.UserFollows.objects.filter(followed_user=user)]

        return render(
            request,
            self.template_name,
            context={
                "name":"Abonnement",
                "searchbox_form": searchbox_form,
                "subscrip_form": formset,
                "helper":helper,
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