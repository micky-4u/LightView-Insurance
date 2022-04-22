from argparse import ONE_OR_MORE
from enum import unique
from itertools import product
from operator import mod
from pickle import TRUE
from django.db import models
from client.models import Client

# Create your models here.
class Products(models.Model):
    product_id = models.BigAutoField(primary_key=True, null = False, unique= TRUE)
    product_name = models.CharField(max_length= 100)
    product_category = models.CharField(max_length=100)
    product_discription = models.CharField(max_length= 200)
    
    def __str__(self):
        return self.product_id

class PolicyType(models.Model):
    policy_type_id = models.BigAutoField(primary_key = True, unique =True)
    type_name = models.CharField(max_length= 60)
    description = models.TextField(max_length= 100)
    has_expired = models.BooleanField()
    monthly_payment = models.DecimalField(max_digits=20, decimal_places=2)
    quarterly_payment =  models.DecimalField(max_digits=20, decimal_places=2)
    yearly_payment = models.DecimalField(max_digits=20, decimal_places=2)
    
class Case(models.Model):
    case_id = models.BigAutoField(unique= True, primary_key= True)
    case_discription = models.TextField(max_length=200)
    
    def __str__(self):
        return self.case_id
    
class Offers(models.Model):
    offer_id = models.BigAutoField(primary_key=True, unique=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete= models.CASCADE)
    policy_type_id = models.ForeignKey(PolicyType, on_delete= models.CASCADE)
    date_signed = models.DateField()
    case_id = models.ForeignKey(Case, on_delete=models.CASCADE)
    premium = models.DecimalField(max_digits= 10, decimal_places= 2)
    terms = models.TextField(max_length=400)
    details = models.TextField(max_length=400)
    is_active = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.offer_id
    
    def get_premuim(self):
        pass
    
    