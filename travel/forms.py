from django.forms import ModelForm 
from django import forms
from .models import *


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'slug']


class AttractionForm(ModelForm):
    more_attraction_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
                    'class':'form-control',
                    'multiple':True
                    }))
    class Meta:
        model = Attraction
        fields = '__all__'        

class ParkForm(ModelForm):
    more_park_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
                    'class':'form-control',
                    'multiple':True
                    }))
    class Meta:
        model = Park
        fields = '__all__'                