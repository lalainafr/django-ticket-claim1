from django.db import models
from django.contrib.auth.models import AbstractUser


# Create custom User Model
class User(AbstractUser):
    is_customer = models.BooleanField()
    is_engineer = models.BooleanField()
    
    def __str__(self) -> str:
        return self.username
