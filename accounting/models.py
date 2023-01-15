from asyncio.windows_events import NULL
from cgitb import text
from pickle import TRUE
# from secrets import choice
from tkinter import Text
from django.db import models
from django.contrib.auth.models import User
from loan.models import Debt



class CustomUser(models.Model):
    def __str__ (self):
      return self.user.username
      
    CHOICES = [
        ('M', 'Male'),
        ('F', 'Famale'),
    ]
    age = models.PositiveIntegerField(null=True)
    phone_number = models.CharField(max_length=11, null = True)
    gender = models.CharField(choices=CHOICES , max_length=20, null=True)
    addres = models.TextField(null=True)
    nationalcode = models.CharField(max_length=10, null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Debt= models.OneToOneField(Debt,on_delete=models.CASCADE)



    
