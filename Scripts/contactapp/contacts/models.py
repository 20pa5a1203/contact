from django.db import models

# Create your models here.

class Contacts(models.Model):
    Name = models.CharField(max_length = 50)
    Phone = models.CharField(max_length = 20)
    Email = models.CharField(max_length = 50)
    Owner = models.CharField(max_length = 50)