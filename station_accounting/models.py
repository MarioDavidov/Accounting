from django.db import models


# Create your models here.
class MonthTable(models.Model):
    tittless = models.CharField(max_length=20)
    jan = models.BooleanField()
    feb = models.BooleanField()
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

