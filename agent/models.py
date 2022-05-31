from django.db import models
from datetime import timezone
from django.contrib.auth.models import User

# Create your models here.


class Agent(models.Model):

    id = models.BigAutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    date_of_birth = models.DateField()
    email = models.EmailField()
    details = models.CharField(max_length=300)
    address = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    stat_date = models.DateField()
    end_date = models.DateField()
    

    def __str__(self):
        return self.last_name 
