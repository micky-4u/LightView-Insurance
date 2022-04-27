from atexit import register
import re
from django.contrib import admin
from .models import Client
# Register your models here.
admin.site.register(Client)