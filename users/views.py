from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from users.models import User
from .form import ResigterUserForm
from django.contrib.auth.forms import *

# registration
def register_user(request):
    if request.method == 'POST':
        form = ResigterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_customer = True
            var.save()
            messages.success(request, 'Votre compte a été créé avec succès. Merci de vous authentifier...')
            return redirect('login')
        else:
            messages.warning(request, f'Echec lors la création du compte...')
            return redirect('register-user')
    else:
        form = ResigterUserForm()
        context ={'form', form}
        return render(request, 'users/register_user.html')    
            
# login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'Bienvenu sur votre page d\'accueil, vous etes bien authentifié(e)...')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Echec lors l\'authentification...')
            return redirect('login')
    else: 
        return render(request, 'users/login.html')
    
#logout
def logout_user(request):
    logout(request)
    messages.success(request, 'Vous êtes bien déconnecté(e)...')
    return redirect('login')
        

