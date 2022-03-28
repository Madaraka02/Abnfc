from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('attractions/<slug:slug>/', attDetails, name="attdetails"),
    path('parks/<slug:slug>/', parkDetails, name="parkdetails"),
    path('search/', search, name='search'),
    path('travel/admin/', admin, name='admin'),
    path('like/<slug:slug>/', like_blog, name="like_blog"),
    path('blogs/<slug:slug>/', blog_details, name="blog_details"),
    path('blogs/', blogs, name="blogs"),
]