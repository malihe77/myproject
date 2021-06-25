from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Favorites(models.Model):    
   
    research_title = models.CharField(max_length=250)    
    slug = models.SlugField(max_length=250, unique_for_date='publish')    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Favorites_posts')    
    Research_content = models.TextField()    
    publish = models.DateTimeField(default=timezone.now)    
    created = models.DateTimeField(auto_now_add=True)    
    updated = models.DateTimeField(auto_now=True)   
    visits = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):        
        return reverse('Favorites:post_detail',                       
                        args=[self.slug])