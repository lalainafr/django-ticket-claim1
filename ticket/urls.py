from django.urls import path
from . import views

urlpatterns = [
    path('create-ticket/', views.create_ticket, name='create-ticket'),
    path('update-ticket/<str:pk>/', views.update_ticket, name='update-ticket'),
    path('ticket-details/<str:pk>/', views.ticket_details, name='ticket-details'),
    path('active-tickets/', views.active_tickets, name='active-tickets')
]