from django.db import models
from client.models import Client

# Create your models here.
class ApplicationDoc(models.Model):
    id = models.BigAutoField(primary_key=True)

    client= models.ForeignKey(Client, related_name="client", on_delete= models.CASCADE)
    licenseType = models.TextChoices("TYPE", "A B C D E F")
    years_of_driving = models.IntegerField()
    insuranceForm = models.FileField(upload_to='doc/')
    RC_Bood = models.FileField(upload_to='doc/')
    identityProof = models.FileField(upload_to='doc/')
            


class Claim (models.Model):
    id = models.BigAutoField(primary_key=True)

    claim_form =  models.FileField(upload_to='doc/')
    policy_documents =  models.FileField(upload_to='doc/')
    chassis_number = models.IntegerField()
    FRI_copy = models.FileField(upload_to='doc/')
    loss_incured = models.DecimalField(max_digits=10, decimal_places= 2)
    vehicle_tax_receipt = models.FileField(upload_to='doc/')
    registration_cet = models.FileField(upload_to='doc/')
    repair_bill = models.DecimalField(max_digits=10, decimal_places= 2)
    surveyor_report = models.FileField(upload_to='doc/')
    police_nonTracable_cet =models.FileField(upload_to='doc/')
    accident_case = models.FileField(upload_to='doc/')
    withness = models.FileField(upload_to='doc/')
    claim_ref = models.IntegerField()