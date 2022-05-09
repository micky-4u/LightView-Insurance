from django.contrib import admin
from .models import Claim, ApplicationDoc
# Register your models here.
admin.site.register(ApplicationDoc)
admin.site.register(Claim)