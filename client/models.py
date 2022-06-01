from django.db import models
from datetime import timezone
from django.contrib.auth.models import User

from agent.models import Agent
# Create your models here.



class Client(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    phone = models.IntegerField()
    date_of_birth = models.DateField()
    details = models.CharField(max_length=300)
    address = models.CharField(max_length=200, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Agent, related_name='clients', on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name