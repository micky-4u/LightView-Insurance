from django.db import models

# Create your models here.


class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    date_of_birth = models.DateField()
    email = models.EmailField()
    details = models.CharField(max_length=300)
    address = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.last_name
