from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save

class Customer(models.Model):
    account      = models.CharField(max_length=20, primary_key=True)
    name         = models.CharField(max_length=50)
    phone        = models.CharField(max_length=13)
    age          = models.PositiveIntegerField()
    address      = models.CharField(max_length=200,default='', null=True)
    balance      = models.DecimalField(default='100.0',decimal_places=2,max_digits=15)
    transactions = models.TextField(default='',null=True)

    def __str__(self):
        return self.account