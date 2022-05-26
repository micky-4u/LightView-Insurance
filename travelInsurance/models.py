from django.db import models

# Create your models here.
class ApplicationDoc (models.Model):
    ctry_of_residence = models.CharField(max_length=50)
    passport_number = models.IntegerField()
    destination = models.CharField(max_length=40)
    departure = models.DateField()
    subcription = models.DateField()
    return_date = models.DateField()
    validity = models.DateField()
    druation = models.IntegerField()
     # flight 
    airline = models.CharField(max_length=50)
    port_dpt = models.CharField(max_length=50)
    transit = models.CharField(max_length=50)
    
class Claim(models.Model):
    pass
