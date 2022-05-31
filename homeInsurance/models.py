from django.db import models

from client.models import Client

# Create your models here.
class ApplicationDocs(models.Model):
    client = models.ForeignKey(Client, related_name="hclient", on_delete=models.CASCADE)
    propertyDoc = models.FileField(upload_to="doc/")
    buildingType = models.CharField(
        max_length=10,
        choices=(("1", "Detached"), ("2", "Semi-detached"), ("3", "Apartement")),
        default="1",
    )
    noOfStories = models.IntegerField()
    valueOfHome = models.DecimalField(max_digits=10, decimal_places=2)
    valueOfHomePlusItems = models.DecimalField(max_digits=10, decimal_places=2)


class Claim(models.Model):
    claim_form = models.FileField(upload_to="doc/")
    policy_documents = models.FileField(upload_to="doc/")
    chassis_number = models.IntegerField()
    loss_incured = models.DecimalField(max_digits=10, decimal_places=2)
    propertyRateReceipt = models.FileField(upload_to="doc/")
    repair_bill = models.DecimalField(max_digits=10, decimal_places=2)
    surveyor_report = models.FileField(upload_to="doc/")
    police_nonTracable_cet = models.FileField(upload_to="doc/")
    accident_case = models.FileField(upload_to="doc/")
    witness = models.FileField(upload_to="doc/")
    claim_ref = models.IntegerField()
