from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from Blogapp.models import Post
from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponse
def home(request):
    return render(request,'home/home.html')
    # return HttpResponse("hello this is a home page")


def about(request):
    messages.success(request, 'this is about page')
    return render(request,'home/about.html')   

def contact(request):
    if request.method== 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<1:
            messages.error(request, "please enter correct information")
        else:    
            contact = Contact(name=name,email=email,content=content,phone=phone)
            contact.save()
            messages.success(request,"your data submitted succesfully")
    return render(request,'home/contact.html')    
def search(request):
    # allPosts = Post.objects.all()
    search = request.GET['search']
    allPosts = Post.objects.filter(title__icontains=search)
    params = {'allPosts':allPosts,'search':search}
    return render(request,'home/search.html', params)


def handleSignup(request):
        if request.method == 'POST':
            # get the post parameter
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email2 = request.POST['email2']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            
            # check for errorneous inputs

            #
            #create the user
            myuser = User.objects.create_user(username,email2,pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "your account has been successfully created")

            return redirect('/home')

        else:
            return HttpResponse('Error 404 page not found')    