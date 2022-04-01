from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('attractions/<slug:slug>/', attDetails, name="attdetails"),
    path('places/<slug:slug>/', parkDetails, name="parkdetails"),
    path('places/', parks, name="parks"),
    path('attractions/', attractions, name="atts"),
    path('search/', search, name='search'),
    path('searchp/', searchp, name='searchp'),
    

    path('like/<slug:slug>/', like_blog, name="like_blog"),
    path('blogs/<slug:slug>/', blog_details, name="blog_details"),
    
    path('blogs/', blogs, name="blogs"),
    path('blog/edit/<int:id>/', edit_blog, name="edit_blog"),
    path('blog/delete/<int:id>/', delete_blog, name="delete_blog"),
    path('addblog/', postblog, name="postblog"),

    path('user/', userposts, name="user"),

    # admin
    path('travel/admin/', admin, name='admin'),
    path('travel/admin/attractions/', admin_atts, name="admin_atts"),
    path('travel/admin/places/', admin_parks, name="admin_parks"),
    path('travel/admin/att/add/', adminatt, name="adminatt"),
    path('travel/admin/park/add/', adminpark, name="adminpark"),
    path('travel/admin/att/edit/<int:id>/', edit_att, name="edit_att"),
    path('travel/admin/place/edit/<int:id>/', edit_park, name="edit_park"),
    path('travel/admin/att/delete/<int:id>/', delete_att, name="delete_att"),
    path('travel/admin/place/delete/<int:id>/', delete_park, name="delete_park"),
]