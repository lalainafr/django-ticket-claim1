from django.urls import path
from . import views

urlpatterns = [
    path('create-ticket/', views.create_ticket, name='create-ticket'),
    path('update-ticket/<str:pk>/', views.update_ticket, name='update-ticket'),
    path('resolve-ticket/<str:pk>/', views.resolve_ticket, name='resolve-ticket'),
    path('ticket-details/<str:pk>/', views.ticket_details, name='ticket-details'),
    path('accept-ticket/<str:pk>/', views.accept_ticket, name='accept-ticket'),
    path('active-tickets/', views.active_tickets, name='active-tickets'),
    path('closed-tickets/', views.closed_tickets, name='closed-tickets'),
    path('engineer-active-tickets/', views.engineer_active_tickets, name='engineer-active-tickets'),
    path('engineer-closed-tickets/', views.engineer_closed_tickets, name='engineer-closed-tickets'),
    path('ticket-queue/', views.ticket_queue, name='ticket-queue')
]
