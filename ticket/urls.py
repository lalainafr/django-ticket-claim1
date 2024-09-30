from django.urls import path
from . import views

urlpatterns = [
    path('create-ticket/', views.create_ticket, name='create-ticket'),
    path('update-ticket/<str:pk>/', views.update_ticket, name='update-ticket'),
    path('resolve-ticket/<str:pk>/', views.resolve_ticket, name='resolve-ticket'),
    path('ticket-details/<str:pk>/', views.ticket_details, name='ticket-details'),
    path('accept-ticket/<str:pk>/', views.accept_ticket, name='accept-ticket'),
    path('active-tickets/', views.active_tickets, name='active-tickets'),
    path('ticket-queue/', views.ticket_queue, name='ticket-queue')
]
