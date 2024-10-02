from django.shortcuts import render
from ticket.models import Ticket

def dashboard(request):
    tickets = Ticket.objects.filter(created_by=request.user)
    eng_tickets = Ticket.objects.filter(assigned_to=request.user)
    context = {'tickets': tickets, 'eng_tickets': eng_tickets}
    return render(request, 'dashboard/dashboard.html', context)    

