from django.db import models
from django.contrib.auth.models import User



# database table to store all places
class Park(models.Model):
    name = models.CharField(max_length=300, unique=True, blank=False)
    location = models.CharField(max_length=300, blank=False)
    image = models.FileField(upload_to='parks')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

# database table to store all attractions
class Attraction(models.Model):
    name = models.CharField(max_length=300, blank=False)
    image = models.FileField(upload_to='attimages')
    description = models.TextField()
    slug = models.SlugField(unique=True)
    parks = models.ManyToManyField(Park, related_name="parks")

    def __str__(self):
        return self.name

# database table to store all multiple images of a specific attraction    
class AttractionImages(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    image = models.FileField(upload_to='attimagesm', blank=True, null=True)

    def __str__(self):
        return self.attraction.name

# database table to store all multiple images of a specific place 
class ParkImages(models.Model):
    park = models.ForeignKey(Park, on_delete=models.CASCADE) 
    image = models.FileField(upload_to='parksm', blank=True, null=True)   

    def __str__(self):
        return self.park.name


# database table to store all blogs
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    snippet =  models.CharField(max_length=300, blank=True, null=True)
    content = models.TextField()
    image = models.FileField(upload_to='blogs', blank=True)
    date_added = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)


    def __str__(self):
        return self.author.username
        
    def total_likes(self):
        return self.likes.count() 

# database table to store user feedback
class Feedback(models.Model):
    name =  models.CharField(max_length=300)
    message = models.TextField() 

    def __str__(self):
        return self.name       