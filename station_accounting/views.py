from django.shortcuts import render, redirect

from station_accounting.forms import AccForm, KasaForm
from station_accounting.models import MonthTable, Kasa


def home_page(request):
    if request.method == 'GET':
        mtable = MonthTable.objects.all()
        kasa_vsichki_tipove = Kasa.objects.all()

        # sybrani_pari = 0
        # for k in mtable:
        #     if k:
        #         a += 5

        def func():
            sybrani_pari = 0
            for k in mtable:
                if k:
                    sybrani_pari += 5
            return sybrani_pari

        context = {
            'form': AccForm(),
            'mtable': mtable,
            'checked': u'\u2705',
            'not_cheked': u'\u274c',
            'kasa_form': KasaForm(),
            'kasa_vsichki_tipove': kasa_vsichki_tipove,
            'funktion': func()
        }

        return render(request, 'home_page.html', context)
    else:
        kasa_form = KasaForm(request.POST)
        if kasa_form.is_valid():
            kasa_form.save()
            return redirect('home')
        form = AccForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'form': AccForm(),
            'kasa_f': KasaForm()
        }
        return render(request, 'home_page.html', context)


def home_page_two(request, pk=None):
    if MonthTable.objects.exists():
        mtable = MonthTable.objects.all()
        context = {
            'mtable': mtable,
        }
        return render(request, 'home_page_two.html', context)
    else:
        mtable = MonthTable.objects.all()
        context = {
            'mtable': mtable,
        }
        return render(request, 'home_page_two.html', context)
