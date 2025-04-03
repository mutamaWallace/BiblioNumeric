from django.db import models
from django.contrib.auth.models import AbstractUser
#   from django.contrib.auth.models import User

# Create your models here.

class Utilisateur(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    cin=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)
    
    
    
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)
    
    class Meta:
        swappable ='AUTH_USER_MODEL'
    