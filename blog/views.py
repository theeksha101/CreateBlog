# views connect models and templates
# In Django, views are responsible for processing requests and returning an HTTP response. 
from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
# {}: This is a dictionary that can be used to pass data to the template.
