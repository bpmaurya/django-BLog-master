from django.shortcuts import render
from .models import Post

# Create your views here.
from django.http import HttpResponse

def bloghome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request, 'blogapp/Bloghome.html',context)
    # return HttpResponse("hello this is blogHome page we will keep all blogpost here")

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    print(post)
    context = {'post':post}
    return render(request, 'Blogapp/Blogpost.html',context)
   