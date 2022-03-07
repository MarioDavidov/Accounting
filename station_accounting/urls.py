from django.urls import path

from station_accounting.views import home_page

urlpatterns = [
    path('', home_page, name='home')

]
