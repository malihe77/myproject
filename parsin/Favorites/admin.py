from django.contrib import admin
from .models import Favorites
# Register your models here.

@admin.register(Favorites) 
class FavoritesAdmin(admin.ModelAdmin):    
    list_display = ('research_title', 'slug', 'author', 'publish', 'visits') 
    list_filter = ('created', 'publish', 'author')    
    search_fields = ('research_title', 'Research_content',)    
    prepopulated_fields = {'slug': ('research_title',)}    
    raw_id_fields = ('author',)    
    date_hierarchy = 'publish'    
    ordering = ('publish',) 
