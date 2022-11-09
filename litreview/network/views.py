from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect
from django.forms import modelformset_factory

from . import forms
from website import models
from network.forms import FollowedUserFormSetHelper


class UserNetwork(LoginRequiredMixin, View):
    template_name='network/subscription.html'
    form_class_search_box = forms.SearchBox
    form_class_followed_user = forms.FollowedUserForm
    
    def get(self, request, *args, **kwargs):
        searchbox_form = self.form_class_search_box()
        
        user = request.user
        followed_users = [x.followed_user for x in models.UserFollows.objects.filter(user=user)]
        print(*followed_users)
        

        followers = [x.user.username for x in models.UserFollows.objects.filter(followed_user=user)]

        return render(
            request,
            self.template_name,
            context={
                "name":"Abonnement",
                "searchbox_form": searchbox_form,
                "followed_users": followed_users,
                "followers": followers,
            }
        )

    def post(self, request, *args, **kwargs):
        if request.POST["search__button"]:
            
            followed_user = User.objects.filter(username=request.POST["username"])[0]
            item = models.UserFollows(user=request.user, followed_user=followed_user)
            item.save()
        searchbox_form = self.form_class_search_box()
        
        user = request.user
        followed_users = [x.followed_user for x in models.UserFollows.objects.filter(user=user)]
        print(*followed_users)
        
        followers = [x.user.username for x in models.UserFollows.objects.filter(followed_user=user)]

        return render(
            request,
            self.template_name,
            context={
                "name":"Abonnement",
                "searchbox_form": searchbox_form,
                "followed_users": followed_users,
                "followers": followers,
            }
        )


class UnfollowUser(LoginRequiredMixin, View):
    template_name = 'network/test.html'
    form_class = ''

    def get(self, request, **kwargs):
        user = request.user
        if request.GET["id"]:
            followed_user = request.GET["id"]
            relation = models.UserFollows.objects.filter(user=user, followed_user__id=followed_user)[0]
            if relation:
                relation.delete()
        # return render(
        #     request,
        #     self.template_name,
        #     context={
        #         "relation":relation
        #     }
        # )
        return redirect("network:subscription", user.username)

    def post(self, request):
        user = request.user
        return redirect("network:subscription", user.username)
