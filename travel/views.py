from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *

def home(request):
    attractions = Attraction.objects.all().order_by('-id')
    parks = Park.objects.all().order_by('-id')
    context = {
        'attractions':attractions,
        'parks':parks,
    }
    return render(request, 'home.html', context)

def attDetails(request, slug):
    att = get_object_or_404(Attraction, slug=slug)    
    images = AttractionImages.objects.filter(attraction=att)
    context = {
        'att':att,
        'images':images,
    }
    return render(request, 'attdetails.html', context)

def parkDetails(request, slug):
    park = get_object_or_404(Park, slug=slug)   
    atts = Attraction.objects.filter(parks__name=park) 
    context = {
        'park':park,
        'atts':atts,
    }
    return render(request, 'parkdetails.html', context)    



# class catlistView(ListView):
#     template_name = "shop/blank.html"
#     context_object_name = 'catlist'


#     def get_queryset(self):
#         content = {
#             'cat': self.kwargs['category'],
#             'items': Product.objects.filter(category__name=self.kwargs['category'])
#         }
#         return content 


def search(request):
    q = request.GET['q']
    if q:
        context = {
            'data' : Attraction.objects.filter(name__icontains=q).order_by('-id'),
        }

        return render(request, 'search.html', context)
            

       
@login_required
def admin(request):
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

                return redirect('admin')    
        context = {
            'form': form,
        }
        return render(request, 'admin.html', context)   

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
    
    return render(request, 'blogdetails.html', context)        

def blogs(request):
    blogs = Blog.objects.all().order_by('-id')    
    context = {
        'blogs':blogs,
    }
    return render(request, 'blogs.html', context)