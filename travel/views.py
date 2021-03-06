from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from .models import *
from .forms import *


# fetching all places and attractions from the database and slicing to display only the latest six
def home(request):
    attractions = Attraction.objects.all().order_by('-id')[:6]
    parks = Park.objects.all().order_by('-id')[:6]
    context = {
        'attractions':attractions,
        'parks':parks,
    }
    return render(request, 'travel/ind.html', context)


# details page for a single attraction fetched using the slug
def attDetails(request, slug):
    att = get_object_or_404(Attraction, slug=slug)    
    images = AttractionImages.objects.filter(attraction=att)
    context = {
        'att':att,
        'images':images,
    }
    return render(request, 'travel/attdetails.html', context)


# details page for a single place fetched using the slug
def parkDetails(request, slug):
    park = get_object_or_404(Park, slug=slug)   
    atts = Attraction.objects.filter(parks__name=park) 
    images = ParkImages.objects.filter(park=park)
    context = {
        'park':park,
        'atts':atts,
        'images':images
    }
    return render(request, 'travel/parkdetails.html', context)    


# search function for an attraction
def search(request):
    q = request.GET['q']
    if q:
        context = {
            'data' : Attraction.objects.filter(name__icontains=q).order_by('-id'),
        }

        return render(request, 'travel/search.html', context)


# search query for a place
def searchp(request):
    p = request.GET['p']
    if p:
        context = {
            'data' : Park.objects.filter(name__icontains=p).order_by('-id'),
        }

        return render(request, 'travel/searchp.html', context)
       

# Main admin function  to display the count of all places and attractions in the database 
# which uses the login required decorator and also checks to make sure the logged in user is an admin
@login_required
def admin(request):
    if request.user.is_staff:
        atts_count = Attraction.objects.all().count()
        place_count = Park.objects.all().count()

        context = {
            'atts_count':atts_count,
            'place_count':place_count,
        }
        return render(request, 'adminn/admin.html', context)
    return redirect('home') 


# admin function for posting an attraction from the frontend
@login_required
def adminatt(request):
    if request.user.is_staff:

        form = AttractionForm()

        if request.method == "POST":
            form = AttractionForm(request.POST, request.FILES)
            files = request.FILES.getlist('more_attraction_images')
            if form.is_valid():
                attraction = form.save()
                for f in files:
                    attraction_image = AttractionImages(attraction=attraction, image=f)
                    attraction_image.save()
                messages.success(request, "attraction was added successfully")
                return redirect('admin_atts')    
        context = {
            'form': form,
        }
        return render(request, 'adminn/att.html', context) 

# admin function for posting a place from the frontend
@login_required
def adminpark(request):
    if request.user.is_staff:

        form = ParkForm()

        if request.method == "POST":
            form = ParkForm(request.POST, request.FILES)
            files = request.FILES.getlist('more_park_images')
            if form.is_valid():
                park = form.save()
                for f in files:
                    park_image = ParkImages(park=park, image=f)
                    park_image.save()
                messages.success(request, "Place was added successfully")
                return redirect('admin_parks')    
        context = {
            'form': form,
        }
        return render(request, 'adminn/park.html', context)


# admin function for fetching and paginating all attractions from the database
@login_required 
def admin_atts(request):
    if request.user.is_staff:
        atts_list = Attraction.objects.all().order_by('-id')
        page = request.GET.get('page', 1)
        paginator = Paginator(atts_list, 15)
        try:
            atts = paginator.page(page)
        except PageNotAnInteger:
            atts = paginator.page(1)
        except EmptyPage:
            atts = paginator.page(paginator.num_pages)  

        context = {
            'atts':atts,
        }  
        return render(request, 'adminn/atts.html', context)    


# admin function for fetching and paginating all places from the database
@login_required 
def admin_parks(request):
    if request.user.is_staff:
        parks_list = Park.objects.all().order_by('-id')
        page = request.GET.get('page', 1)
        paginator = Paginator(parks_list, 15)
        try:
            parks = paginator.page(page)
        except PageNotAnInteger:
            parks = paginator.page(1)
        except EmptyPage:
            parks = paginator.page(paginator.num_pages)  

        context = {
            'parks':parks,
        }  
        return render(request, 'adminn/places.html', context)


# admin function for updating an attraction
@login_required
def edit_att(request, id):
    if request.user.is_staff:
        att = get_object_or_404(Attraction, id = id)
        

        form = AttractionForm(request.POST or None, instance=att)
        if form.is_valid():
            form.save()
            messages.success(request, "attraction was updated successfully")
            return redirect('admin_atts')
        context = {
            'att':att,
            'form':form,
        }
        return render(request, 'adminn/updateatt.html', context)  


# admin function for updating a place
@login_required
def edit_park(request, id):
    if request.user.is_staff:
        park = get_object_or_404(Park, id = id)
        

        form = ParkForm(request.POST or None, instance=park)
        if form.is_valid():
            form.save()
            messages.success(request, "place was updated successfully")
            return redirect('admin_parks')
        context = {
            'park':park,
            'form':form,
        }
        return render(request, 'adminn/updatepark.html', context)  


# admin function for deleting an attraction from the database
@login_required
def delete_att(request, id):
    if request.user.is_staff:
        att = get_object_or_404(Attraction, id = id)
        att.delete()
        messages.success(request, "Attraction was deleted successfully")
        return redirect('admin_atts')


# admin function for deleting a place from the database
@login_required
def delete_park(request, id):
    if request.user.is_staff:
        park = get_object_or_404(Park, id = id)
        park.delete()
        messages.success(request, "Park was deleted successfully")
        return redirect('admin_parks')


# function to trigger the like blog method
def like_blog(request, slug):
    blog = get_object_or_404(Blog, slug=request.POST.get('blog_slug'))  
    is_liked = False
    if   blog.likes.filter(id= request.user.id).exists():
        blog.likes.remove(request.user)
        is_liked = False
    else:
        blog.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(reverse('blog_details', args=[str(slug)]))

# function for displaying blog details by fetching a specific blog using its slug
def blog_details(request, slug):
    
    blog = get_object_or_404(Blog, slug=slug)
    is_liked = False
    if  blog.likes.filter(id= request.user.id).exists():
        is_liked=True

    
    context = {
        'blog':blog,
        'total_likes':blog.total_likes(),
        'is_liked':is_liked,
    }
    
    return render(request, 'travel/blogdetails.html', context)        


# function for fetching all blogs from the database
def blogs(request):
    
    blogss = Blog.objects.all().order_by('-id')
    

    paginator = Paginator(blogss, 6)

    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)
    context = {
        'blogs':blogs,
    }
    return render(request, 'travel/blogs.html', context)


# function for fetching a specific blog to be updated using its id
@login_required
def edit_blog(request, id):
    blog = get_object_or_404(Blog, id = id)
    

    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        messages.success(request, "Your blog was updated successfully")
        return redirect('user')
    context = {
        'blog':blog,
        'form':form,
    }
    return render(request, 'travel/updateblog.html', context)    


# function for posting new blogs from the frontend
@login_required
def postblog(request):
    if request.user.is_authenticated:
        form = BlogForm() 
        if request.method == "POST":
            form = BlogForm(request.POST, request.FILES)
           
            
            if form.is_valid():  
                blog = form.save(commit=False)   
                blog.author = request.user
                blog.save()
                messages.success(request, "Your blog was added")
                return redirect('home')
    
        context = {
            'form':form,
        }
        return render(request, 'travel/postblogpage.html', context)


# function for fetching a specific blog using its id and deleting it
@login_required
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id = id)
    blog.delete()
    messages.success(request, "Your blog was deleted successfully")
    return redirect('user')


# function for fetching all the blogs of the current logged in use
@login_required
def userposts(request):
    blogss = Blog.objects.filter(author=request.user.id).order_by('-id')
    

    paginator = Paginator(blogss, 3)

    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)
    context ={
        'blogs':blogs,
      
    }
    return render(request, 'travel/users.html', context)   


# function to fetch all places in the database and ordering them by the latest id
def parks(request):
       
    parkss = Park.objects.all().order_by('-id')
    

    paginator = Paginator(parkss, 1)

    page_number = request.GET.get('page')
    parks = paginator.get_page(page_number)
    context = {
        'parks':parks,
    }
    return render(request, 'travel/parks.html', context)


# function for fetching all attractions and ordering them by the latest id
def attractions(request):
    attractionss = Attraction.objects.all().order_by('-id') 

    paginator = Paginator(attractionss, 1)

    page_number = request.GET.get('page')
    attractions = paginator.get_page(page_number)
    context = {
        'attractions':attractions,
    }
    return render(request, 'travel/atts.html', context)        