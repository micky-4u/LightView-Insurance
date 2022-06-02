from django.contrib import admin
from .models import Claim, Application,Quote
# Register your models here.
admin.site.register(Application)
admin.site.register(Claim)
admin.site.register(Quote)