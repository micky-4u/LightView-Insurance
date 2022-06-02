from django.db import models
from datetime import timezone
from django.contrib.auth.models import User

from agent.models import Agent
# Create your models here.
import uuid

code = uuid.uuid1()


class Client(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    phone = models.IntegerField()
    client_code =  models.IntegerField( blank=True, default= code.node, auto_created=True)
    nationality = models.CharField(max_length=100)
    national_id = models.CharField(max_length=100)
    id_number = models.PositiveIntegerField()
    tin = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Agent, related_name='clients', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.last_name
    
    
    @property
    def set_client_code(self):
        self.client_code = code.time