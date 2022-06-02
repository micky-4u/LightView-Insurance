from django.db import models
from datetime import timezone
from django.contrib.auth.models import User
import uuid
# Create your models here.
codes = uuid.uuid1()

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    phone = models.IntegerField()
    agent_code = models.IntegerField(max_length=100, blank=True, default= codes.time, auto_created=True)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    national_id = models.CharField(max_length=100)
    id_number = models.PositiveIntegerField()
    tin = models.PositiveIntegerField()
    address = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.user.first_name


