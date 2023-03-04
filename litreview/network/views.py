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
        
        # display users followed by the login user
        user = request.user
        followed_users = [x.followed_user for x in models.UserFollows.objects.filter(user=user)]
        
        # display users who follow the login user
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
        # display the search box form              
        searchbox_form = self.form_class_search_box()
        
        # display users followed by the login user
        user = request.user
        followed_users = [x.followed_user for x in models.UserFollows.objects.filter(user=user)]
        
        # display users who follow the login user
        followers = [x.user.username for x in models.UserFollows.objects.filter(followed_user=user)]

        # user clicked on the search__button
        search_messages = []
        if request.POST["search__button"]:
            user_input = request.POST["username"]
            try:
                input_validation = True
                follow_user = User.objects.get(username=user_input)
                if follow_user == request.user:
                    input_validation = False
                    search_messages.append("Vous ne pouvez pas vous suivre vous-même")
                if follow_user in followed_users:
                    input_validation = False
                    search_messages.append(f'Vous suivez déjà {user_input}')

                if input_validation:
                    item = models.UserFollows(user=request.user, followed_user=follow_user)
                    item.save()
                    # update list of followed people
                    followed_users = [x.followed_user for x in models.UserFollows.objects.filter(user=user)]
            
            except BaseException as err:
                print(f'DEBUG : {err}') 
                search_messages.append(f"l'utilisateur {user_input} n'existe pas")
        
        return render(
            request,
            self.template_name,
            context={
                "name":"Abonnement",
                "search_messages": search_messages,
                "searchbox_form": searchbox_form,
                "followed_users": followed_users,
                "followers": followers,
            }
        )


class UnfollowUser(LoginRequiredMixin, View):
    form_class = ''

    def get(self, request, **kwargs):
        user = request.user
        if request.GET["id"]:
            followed_user = request.GET["id"]
            relation = models.UserFollows.objects.filter(user=user, followed_user__id=followed_user)[0]
            if relation:
                relation.delete()
        return redirect("network:subscription", user.username)

    def post(self, request):
        user = request.user
        return redirect("network:subscription", user.username)
