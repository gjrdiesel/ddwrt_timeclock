from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Employee,TimePeriod,StateChange,Hostname

admin.site.register(Employee)
admin.site.register(TimePeriod)
admin.site.register(StateChange)
admin.site.register(Hostname)
