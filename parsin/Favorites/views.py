from django.shortcuts import render, get_object_or_404 
from .models import Favorites
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):    
    object_list = Favorites.objects.filter(status='published')   
    paginator = Paginator(object_list, 3) # 3 posts in each page    
    page = request.GET.get('page')    
    try:        
         posts = paginator.page(page)    
    except PageNotAnInteger:        
        # If page is not an integer deliver the first page        
        posts = paginator.page(1)    
    except EmptyPage:        
    # If page is out of range deliver last page of results        
        posts = paginator.page(paginator.num_pages)    
    
    return render(request,'Favorites/post/list.html',                   
                            {'page': page, 
                            'posts': posts}) 

def post_detail(request, post):    
    post = get_object_or_404(Favorites, slug=post,                                   
            status='published',                                   
            publish__year=year,                                   
            publish__month=month,                                   
            publish__day=day)
    Favorites.visits = Favorites.visits + 1
    Favorites.save()  
    return render(request,                  
    'Favorites/post/detail.html',                  
    {'post': post}) 