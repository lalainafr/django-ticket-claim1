from django.shortcuts import render, redirect
from users.models import User
from .form import CreateTicketForm, UpdateTicketForm
from django.contrib import messages
from .models import Ticket

""" For All """

# ticket details
def ticket_details(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    context = {'ticket': ticket}
    return render(request, 'ticket/ticket_details.html', context)


""" For Customers """

# creating ticket
def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.user
            var.ticket_status = 'Pending'
            var.save()
            
            messages.success(request, 'Le ticket a été soumis')
            return redirect('active-tickets')
        else:
            messages.warning(request, 'Echec lors de la création du ticket')
            return redirect('dashboard')

    else:
        form = CreateTicketForm()
        context = {'form': form}
        return render(request, 'ticket/create_ticket.html', context)

# updating ticket
def update_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, 'Le ticket a été mis à jour')
            return redirect('active-tickets')
        else:
            messages.warning(request, 'Echec lors de la création du ticket')
            return redirect('dashboard')

    else:
        form = UpdateTicketForm( instance=ticket)
        context = {'form': form}
        return render(request, 'ticket/update_ticket.html', context)
    
# active tickets
def active_tickets(request):
    tickets = Ticket.objects.filter(created_by=request.user)
    context = {'tickets': tickets}
    return render(request, 'ticket/active_tickets.html', context)

""" For Engineer """

# ticket queue
def ticket_queue(request):
    tickets =  Ticket.objects.filter(ticket_status='Pending')
    context = {'tickets': tickets}
    return render(request, 'ticket/ticket_queue.html', context)