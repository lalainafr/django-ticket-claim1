from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from users.models import User
from .form import ResigterUserForm
from django.contrib.auth.forms import *
from django.core.mail import send_mail
from django.views.generic import View

# token - mail confirmation import
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .token import TokenGenerator, generate_token
from django.utils.encoding import force_bytes, force_str
from django.conf import settings
from django.contrib.auth import get_user_model


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        # on decode le pk et on le compare si ca correspond à l'id du user
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as identifier:
        user = None
        
    # on decode le token et le compare par rapport au token generé   
    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()     
        messages.success(request, f'Votre compte a été activé, pour pouvez vous authentifier actuelement..')
        return redirect('login') 
    return render (request, 'users/activate_fail.html')  
    

# registration
def register_user(request):
    if request.method == 'POST':
        form = ResigterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            if user.is_engineer:
                user.is_engineer =  True
            else:
                user.is_customer =  True
    
            user.save()
            
            # email content
            email_subject="Activer votre compte"
            message = render_to_string('users/activate.html', {
                'user ': user,
                'domain':'127.0.0.1:8000',
                # encoder le user.pk
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # generer un token pour le user.pk
                'token': generate_token.make_token(user)
            })
            
            messages.success(request, f'Votre compte a été créé avec succès. Merci de confirmer votre compte dans le mail qui vous a été envoyé..')
            
             # send mail
            email_from = 'lalaina@myself.com'
            recipient_list = [user.email]
            send_mail(email_subject, message, email_from, recipient_list)
            
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
        

