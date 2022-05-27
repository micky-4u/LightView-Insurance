from django.db import models
from datetime import timezone

from agent.models import Agent
# Create your models here.



class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    date_of_birth = models.DateField()
    email = models.EmailField()
    details = models.CharField(max_length=300)
    address = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    #created_by = models.ForeignKey(Agent, related_name='clients', on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name