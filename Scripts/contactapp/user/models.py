from django.db import models

# Create your models here.

class User_Master(models.Model):
    Email = models.CharField(max_length = 50)
    Password = models.CharField(max_length =50)
    Secret = models.CharField(max_length = 50)
    