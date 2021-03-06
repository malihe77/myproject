from django.db import models 
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):    
    STATUS_CHOICES = (        
        ('draft', 'Draft'),        
        ('published', 'Published'),    
    )    
    research_title = models.CharField(max_length=250)    
    slug = models.SlugField(max_length=250, unique_for_date='publish')    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')    
    Research_content = models.TextField()    
    publish = models.DateTimeField(default=timezone.now)    
    created = models.DateTimeField(auto_now_add=True)    
    updated = models.DateTimeField(auto_now=True)    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    visits = models.PositiveIntegerField(default=0)
    email = models.EmailField(max_length=128, help_text='Email Address')

    class Meta:        
        ordering = ('-publish',)
    def __str__(self):        
        return self.research_title

    def get_absolute_url(self):        
        return reverse('list_topic:post_detail',                       
        args=[self.publish.year, self.publish.month, self.publish.day, self.slug])