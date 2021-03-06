from django.shortcuts import render, get_object_or_404 
from .models import Post
from .forms import EmailPostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):    
    object_list = Post.objects.filter(status='published')   
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
    
    return render(request,'list_topic/post/list.html',                   
                            {'page': page, 
                            'posts': posts}) 

def post_detail(request, year, month, day, post):    
    post = get_object_or_404(Post, slug=post,                                   
            status='published',                                   
            publish__year=year,                                   
            publish__month=month,                                   
            publish__day=day)
    post.visits = post.visits + 1
    post.save()  
    return render(request,                  
    'list_topic/post/detail.html',                  
    {'post': post}) 

def post_share(request, post_id):    
    # Retrieve post by id    
    post = get_object_or_404(Post, id=post_id, status='published')
     if request.method == 'POST':        
        # Form was submitted        
        form = EmailPostForm(request.POST)        
        if form.is_valid():            
            # Form fields passed validation            
            cd = form.cleaned_data            
            # ... send email    
    else:        
        form = EmailPostForm()    
    return render(request,'list_topic/post/share.html', {'post': post,
                                                        'form': form}) 
