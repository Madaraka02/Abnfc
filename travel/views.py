from django.shortcuts import get_object_or_404, render
from .models import *

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
    context = {
        'park':park,
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
            'data' : Product.objects.filter(name__icontains=q).order_by('-id'),
        }

        return render(request, 'shop/search.html', context)
            