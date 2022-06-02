from pyexpat import model
from tkinter.tix import Tree
from django.db import models
from client.models import Client
import uuid

code = uuid.uuid1()
# Create your models here.
class Quote(models.Model):
    id = models.BigAutoField(primary_key=True)

    cover_type = models.CharField(
        max_length=100,
        choices=(
            ("1", "THIRD PARTY ONLY"),
            ("2", "THIRD PARTY FIRE AND THEFT"),
            ("3", "COMPREHENSIVE"),
        ),
        default="1",
        
        )
    usage = models.CharField( max_length=100 )
    num_of_seats = models.PositiveIntegerField()
    value_of_vehicle = models.PositiveIntegerField()
    period =models.CharField(max_length=100)
    extra_TTPD = models.IntegerField(null=True,blank=True)
    excess_buy_back = models.CharField(max_length=100,null=True,blank=True,)
    premium = models.PositiveIntegerField()
    
    def __str__(self):
        return self.premium
    
    
class Application(models.Model):
    client = models.ForeignKey(Client, related_name="clients", on_delete=models.CASCADE)
    motoinc_reg = models.PositiveIntegerField()
    vehicle_registration_number = models.CharField(max_length=100)
    make_of_vehicle = models.CharField(max_length=100)
    vehicle_body_type = models.CharField(max_length=100)
    vehicle_cubic_capacity = models.CharField(max_length=100)
    year_of_manufacture = models.DateField()
    vehicle_color = models.CharField(max_length=100)
    vehicle_chassis_num = models.PositiveIntegerField() 
    
    def __str__(self):
        return self.motoinc_reg
    
    @property
    def get_reg_num(self):
        self.motoinc_reg = code.node




class Claim(models.Model):
    client = models.ForeignKey(Client, related_name="mclient", on_delete=models.CASCADE)
    motoinc_reg = models.PositiveIntegerField()
    driver_name = models.CharField(max_length=100)
    driver_licence = models.IntegerField()
    date_time = models.DateTimeField()
    acc_location = models.CharField(max_length=200)
    claim_doc = models.FileField(upload_to="doc/")

