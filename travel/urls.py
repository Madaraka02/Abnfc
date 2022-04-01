from django.urls import path
from .views import *

urlpatterns = [
    # the homepage url
    path('', home, name="home"),
    # url to a single attraction details page
    path('attractions/<slug:slug>/', attDetails, name="attdetails"),
    # url to a single place details page
    path('places/<slug:slug>/', parkDetails, name="parkdetails"),
    # url to all places page
    path('places/', parks, name="parks"),
    # url to all attractions page
    path('attractions/', attractions, name="atts"),
    # url to an attraction search results page
    path('search/', search, name='search'),
    # url to a place search results page
    path('searchp/', searchp, name='searchp'),
    
    # url to liking a single blog
    path('like/<slug:slug>/', like_blog, name="like_blog"),
    # url to a single blog page
    path('blogs/<slug:slug>/', blog_details, name="blog_details"),
    
    # url to all blogs page
    path('blogs/', blogs, name="blogs"),
    # url to a single blog edit page
    path('blog/edit/<int:id>/', edit_blog, name="edit_blog"),
    # url to a delete a single blog 
    path('blog/delete/<int:id>/', delete_blog, name="delete_blog"),
    # url to post a blog
    path('addblog/', postblog, name="postblog"),

    # url to a users dashboard page
    path('user/', userposts, name="user"),

    # admin urls
    # url to admin's home page
    path('travel/admin/', admin, name='admin'),
    # url to admin's attractions page
    path('travel/admin/attractions/', admin_atts, name="admin_atts"),
    # url to admin's places page
    path('travel/admin/places/', admin_parks, name="admin_parks"),
    # url to admin's attractions add page
    path('travel/admin/att/add/', adminatt, name="adminatt"),
    # url to admin's parks add page
    path('travel/admin/park/add/', adminpark, name="adminpark"),
    # url to admin's attractions edit page
    path('travel/admin/att/edit/<int:id>/', edit_att, name="edit_att"),
    # url to admin's places edit page
    path('travel/admin/place/edit/<int:id>/', edit_park, name="edit_park"),
    # url to admin's attractions delete page
    path('travel/admin/att/delete/<int:id>/', delete_att, name="delete_att"),
    # url to admin's places delete page
    path('travel/admin/place/delete/<int:id>/', delete_park, name="delete_park"),
]