from django.db import models
from client.models import Client

# Create your models here.
class ApplicationDoc(models.Model):
    id = models.BigAutoField(primary_key=True)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    adhaar = models.FileField(upload_to='doc/')
    derivers_license = models.FileField(upload_to='doc/')
    passport = models.FileField(upload_to='doc/')
    adhaar = models.FileField(upload_to='doc/')
    pan_card = models.FileField(upload_to='doc/')
    salary_slip = models.FileField(upload_to='doc/')
    bank_statement = models.FileField(upload_to='doc/')
    itr = models.FileField(upload_to='doc/')

    class Mata: 
        ordering = ["client"]
# class Claim (models.Model):
#     pass