from django.contrib import admin
from .models import PolicyType, Products, Case, Offers, MotoInsurance
# Register your models here.
admin.site.register(PolicyType)
admin.site.register(Products)
admin.site.register(Case)
admin.site.register(Offers)
admin.site.register(MotoInsurance)