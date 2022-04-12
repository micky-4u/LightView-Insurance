from enum import unique
from itertools import product
from operator import mod
from pickle import TRUE
from django.db import models

# Create your models here.
class Products(models.Model):
    product_id = models.BigAutoField(primary_key=True, null = False, unique= TRUE)
    product_name = models.CharField(max_length= 100)
    product_category = models.CharField(max_length=100)
    product_discription = models.CharField(max_length= 200)
    
    
class Offers(models.Model):
    offer_id = models.BigAutoField(primary_key=True, unique=True)
    client_id = models.ForeignKey()
    has_role_id = models.ForeignKey()
    product_id = models.ForeignKey(Products, on_delete= models.CASCADE())
    policy_type_id = models.ForeignKey()
    date_signed = models.DateField()
    case_id = models.ForeignKey()
    premium = models.DecimalField(max_digits= 10, decimal_places= 2)
    terms = models.TextField(max_length=400)
    details = models.TextField(max_length=400)
    is_active = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    
class Case(models.Model):
    case_id = models.BigAutoField(unique= True, primary_key= True)
    case_discription = models.TextField(max_length=200)