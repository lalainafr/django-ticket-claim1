from django.shortcuts import render, redirect
from users.models import User
from .form import CreateTicketForm
from django.contrib import messages

""" For Customers """

# creating ticket
def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.customer = request.user
            var.status = 'Pending'
            var.save()
            
            messages.success(request, 'Le ticket a été soumis')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Echec lors de la création du ticket')
            return redirect('dashboard')

    else:
        form = CreateTicketForm()
        context = {'form': form}
        return render(request, 'ticket/create_ticket.html', context)