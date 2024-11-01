from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user, name='register-user'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]