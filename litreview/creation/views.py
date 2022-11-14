from django.shortcuts import render, redirect

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from creation.forms import CreateTicket



# Create your views here.
class CreationTicketView(LoginRequiredMixin, View):
    template_name = 'creation/ticket_creation.html'
    form_class_creation_ticket = CreateTicket

    def get(self, request, *args, **kwargs):
        ticket_creation = self.form_class_creation_ticket()
        return render(
            request,
            self.template_name,
            context = {
            'form':ticket_creation,
            }
        )
    
    def post(self, request, *args, **kwargs):
        if ticket_creation.is_valid():
            ticket_creation = self.form_class_creation_ticket(request.POST, request.FILES)
            ticket = ticket_creation.save(commit=False)
            ticket.user = request.user
            ticket.save()
        else:
            ticket_creation = self.form_class_creation_ticket()
            return render(
                request,
                self.template_name,
                context = {
                    'form':ticket_creation
                }
            )
    