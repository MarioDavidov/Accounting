from django.db import models


# Create your models here.
class MonthTable(models.Model):
    jan = models.BooleanField(editable=True)
    feb = models.BooleanField(editable=True)
    march = models.BooleanField(editable=True)
    april = models.BooleanField(editable=True)
    may = models.BooleanField(editable=True)
    june = models.BooleanField(editable=True)
    july = models.BooleanField(editable=True)
    august = models.BooleanField(editable=True)
    sept = models.BooleanField(editable=True)
    oct = models.BooleanField(editable=True)
    nove = models.BooleanField(editable=True)
    dec = models.BooleanField(editable=True)

