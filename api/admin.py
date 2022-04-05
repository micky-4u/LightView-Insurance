from django.contrib import admin

# Register your models here.

from .models import Agent, Client

admin.site.register(Client)
admin.site.register(Agent)
