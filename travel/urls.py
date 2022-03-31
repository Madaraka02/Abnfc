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
    path('blog/edit/<int:id>/', edit_blog, name="edit_blog"),
    path('blog/delete/<int:id>/', delete_blog, name="delete_blog"),
    path('addblog/', postblog, name="postblog"),

    path('user/', userposts, name="user"),
]