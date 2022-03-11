from django.shortcuts import render, redirect

from station_accounting.forms import AccForm
from station_accounting.models import MonthTable


def home_page(request):
    if request.method == 'GET':
        mtable = MonthTable.objects.all()
        context = {
            'form': AccForm(),
            'mtable': mtable,
        }
        return render(request, 'home_page.html', context)
    else:
        form = AccForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_two')
        context = {
            'form': AccForm(),

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
