from django.db import models

# Create your models here.
class ApplicationDoc(models.Model):
    adhaar = models.FileField(upload_to='doc/')
    derivers_license = models.FileField(upload_to='doc/')
    passport = models.FileField(upload_to='doc/')
    adhaar = models.FileField(upload_to='doc/')
    pan_card = models.FileField(upload_to='doc/')
    salary_slip = models.FileField(upload_to='doc/')
    bank_statement = models.FileField(upload_to='doc/')
    itr = models.FileField(upload_to='doc/')

class Claim (models.Model):
    pass