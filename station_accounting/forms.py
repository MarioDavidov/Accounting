from django import forms

from station_accounting.models import MonthTable, Kasa


class AccForm(forms.ModelForm):
    class Meta:
        model = MonthTable
        fields = '__all__'


class KasaForm(forms.ModelForm):
    class Meta:
        model = Kasa
        fields = '__all__'
