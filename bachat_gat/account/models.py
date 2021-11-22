from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Register(models.Model):
    fname = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()

    