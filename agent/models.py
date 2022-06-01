from django.db import models
from datetime import timezone
from django.contrib.auth.models import User

# Create your models here.


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    phone = models.IntegerField()
    date_of_birth = models.DateField()
    details = models.CharField(max_length=300)
    address = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.user.first_name
