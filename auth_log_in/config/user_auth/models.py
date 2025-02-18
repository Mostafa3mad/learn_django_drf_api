from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20,blank=True,null=True)
    gender = models.CharField(max_length=10, choices=(('male', 'male'), ('female', 'female')),blank=True, null=True)
    age = models.PositiveIntegerField(blank=False, null=False)
    def __str__(self):
        return self.username
