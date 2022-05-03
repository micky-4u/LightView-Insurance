from django.db import models
from client.models import Client

# Create your models here.
class MotoInsurance(models.Model):
    client_id = models.ForeignKey(Client, on_delete= models.CASCADE)
    licenseType = models.TextChoices("TYPE", "A B C D E F")
    years_of_driving = models.IntegerField(max_length=4)
    premium = models.DecimalField(max_digits= 10, decimal_places= 2)
    insuranceForm = models.FileField(upload_to='doc/')
    RC_Bood = models.FileField(upload_to='doc/')
    identityProof = models.FileField(upload_to='doc/')

    @property
    def get_premuim(self):
        if self.years_of_driving >= 4:
            self.premium = 100
        else: 
            self.premium = 300
