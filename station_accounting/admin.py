from django.contrib import admin

# Register your models here.
from station_accounting.models import MonthTable, Kasa

admin.site.register(MonthTable)
admin.site.register(Kasa)