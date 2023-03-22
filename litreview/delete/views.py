from django.shortcuts import render

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from website import models


class reviewDeletion(LoginRequiredMixin, View):
    template_name = 'delete/delete.html'

    def get(self, request, *args, **kwargs):
        try:
            post = models.Review.objects.get(id=request.GET['review_id'])
            post.delete()
            message = "la revue a été supprimé"
        except:
            message = "la revue n'a pas pu être trouvé"

        return render(
            request,
            self.template_name,
            context={
                'title': 'Supprimer une revue',
                'message': message,
                'user': request.user,
            }
        )


class ticketDeletion(LoginRequiredMixin, View):
    template_name = 'delete/delete.html'

    def get(self, request, *args, **kwargs):
        try:
            post = models.Ticket.objects.get(id=request.GET['ticket_id'])
            print('try block')
            post.delete()
            message = "le ticket et les revues associées ont été supprimés"
        except:
            print("error")
            message = "le ticket n'a pas pu être trouvé"

        return render(
            request,
            self.template_name,
            context={
                'title': 'Supprimer ticket',
                'message': message,
                'user': request.user,
            }
        )
