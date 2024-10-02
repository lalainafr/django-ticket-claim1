from django.shortcuts import render, redirect
from users.models import User
from .form import CreateTicketForm, UpdateTicketForm
from django.contrib import messages
from .models import Ticket
import datetime
from django.contrib.auth.decorators import login_required


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
    tickets = Ticket.objects.filter(created_by=request.user, is_resolved = False)
    context = {'tickets': tickets}
    return render(request, 'ticket/active_tickets.html', context)

# closed tickets
def closed_tickets(request):
    tickets = Ticket.objects.filter(created_by=request.user, is_resolved = True)
    context = {'tickets': tickets}
    return render(request, 'ticket/closed_tickets.html', context)

# resolved tickets
def resolve_tickets(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    context = {'ticket': ticket}
    ticket.ticket_status = 'Completed'
    ticket_accepted_date =  datetime.datetime.now()
    ticket.save()
    messages.success(request, f'Le ticket a été clôturé par {request.user}')
    return redirect('ticket-queue')
    

""" For Engineer """


# ticket queue
@login_required
def ticket_queue(request):
    tickets =  Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'ticket/ticket_queue.html', context)


# Engineer active ticket
def engineer_active_tickets(request):
    tickets =  Ticket.objects.filter(assigned_to= request.user, is_resolved=False)
    context = {'tickets': tickets}
    return render(request, 'ticket/engineer_active_tickets.html', context)

# Engineer Closed ticket
def engineer_closed_tickets(request):
    tickets =  Ticket.objects.filter(assigned_to= request.user, is_resolved=True)
    context = {'tickets': tickets}
    return render(request, 'ticket/engineer_closed_tickets.html', context)

# assign ticket
def accept_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.assigned_to = request.user
    ticket.ticket_status = 'Active'
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    messages.success(request, f'Le ticket a été pris en charge par {request.user}')
    return redirect('ticket-queue')

# resolve ticket
def resolve_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.is_resolved =  True
    ticket.ticket_status = 'Completed'
    ticket.closed_date = datetime.datetime.now()
    ticket.save()
    messages.success(request, f'Le ticket a été cloturé par {request.user}')
    return redirect('ticket-queue')
     