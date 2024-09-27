from users.models import User
from django.contrib.auth.forms import UserCreationForm

class ResigterUserForm(UserCreationForm):
    class Meta:
        model =  User
        fields =['username', 'email', 'password1', 'password2']