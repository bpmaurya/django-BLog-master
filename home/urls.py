# from Blog.Blogapp.views import Blog
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [

    path('',views.home,name="home"),
    path('contact/',views.contact, name="contact"),
    path('about/',views.about,name="about"),
    path('search/',views.search,name="search"),
    path('signup/',views.handleSignup,name="handleSignup")
]
