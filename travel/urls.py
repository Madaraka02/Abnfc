from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('attractions/<slug:slug>/', attDetails, name="attdetails"),
    path('parks/<slug:slug>/', parkDetails, name="parkdetails"),
    path('search/', search, name='search'),
    path('travel/admin/', admin, name='admin'),
]