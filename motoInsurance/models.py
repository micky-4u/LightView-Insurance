from django.db import models
from client.models import Client

# Create your models here.
class ApplicationDoc(models.Model):
    id = models.BigAutoField(primary_key=True)

    client = models.ForeignKey(Client, related_name="mclient", on_delete=models.CASCADE)
    licenseType = models.CharField(
        max_length=10,
        choices=(
            ("1", "A"),
            ("2", "B"),
            ("3", "C"),
            ("4", "D"),
            ("5", "E"),
            ("6", "F"),
        ),
        default="1",
    )
    years_of_driving = models.IntegerField()
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    insuranceForm = models.FileField(upload_to="doc/")
    RC_Bood = models.FileField(upload_to="doc/")
    identityProof = models.FileField(upload_to="doc/")

    @property
    def get_premuim(self):
        if self.years_of_driving >= 4:
            self.premium = 100
        else:
            self.premium = 300


class Claim(models.Model):
    id = models.BigAutoField(primary_key=True)

    claim_form = models.FileField(upload_to="doc/")
    policy_documents = models.FileField(upload_to="doc/")
    chassis_number = models.IntegerField()
    FRI_copy = models.FileField(upload_to="doc/")
    loss_incured = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle_tax_receipt = models.FileField(upload_to="doc/")
    registration_cet = models.FileField(upload_to="doc/")
    repair_bill = models.DecimalField(max_digits=10, decimal_places=2)
    surveyor_report = models.FileField(upload_to="doc/")
    police_nonTracable_cet = models.FileField(upload_to="doc/")
    accident_case = models.FileField(upload_to="doc/")
    withness = models.FileField(upload_to="doc/")
    claim_ref = models.IntegerField()
