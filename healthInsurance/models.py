from django.db import models

# Create your models here.
class ApplicationDoc(models.Model):
    application_form = models.FileField(upload_to='doc/')
    statementOfHealth_form = models.FileField(upload_to='doc/')
    birth_certificate = models.FileField(upload_to='doc/')
    passport = models.FileField(upload_to='doc/')
    voting_id_copy = models.FileField(upload_to='doc/')
    voting_id = models.IntegerField()
    driving_license = models.FileField(upload_to='doc/')
    electricity_bill= models.FileField(upload_to='doc/')
    date = models.DateField()


class Claim(models.Model):
    claim_form = models.FileField(upload_to='doc/')
    discharge_card = models.FileField(upload_to='doc/')
    doctors_report = models.FileField(upload_to='doc/')
    hospital_bill =models.FileField(upload_to='doc/')
    x_ray_film = models.FileField(upload_to='doc/')
    other_documents= models.FileField(upload_to='doc/')
