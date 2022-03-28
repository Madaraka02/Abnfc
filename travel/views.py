from django.shortcuts import get_object_or_404, render, redirect
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
    context = {
        'att':att,
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