from django.urls import path

from station_accounting.views import home_page, home_page_two

urlpatterns = [
    path('', home_page, name='home'),
    path('home_two/', home_page_two, name='home_two')

]
