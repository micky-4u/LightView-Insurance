from django.db import models
from datetime import timezone
# Create your models here.


class Agent(models.Model):
    created_by = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)

    id = models.BigAutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    date_of_birth = models.DateField()
    email = models.EmailField()
    details = models.CharField(max_length=300)
    address = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    stat_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey('auth.User', related_name='agents', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['is_active']

    def __str__(self):
        return self.last_name
