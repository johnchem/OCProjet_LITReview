from django.shortcuts import render

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from creation.forms import CreateTicket



# Create your views here.
class CreationTicketView(LoginRequiredMixin, View):
    template_name = 'creation/creation_ticket.html'
    form_class_creation_ticket = CreateTicket

    def post(self, request):
        ticket_creation = self.form_class_creation_ticket()

        

