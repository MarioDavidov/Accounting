from django import forms

from station_accounting.models import MonthTable


class AccForm(forms.ModelForm):
    class Meta:
        model = MonthTable
        fields = '__all__'
