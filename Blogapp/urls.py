# from Blog.Blogapp.views import Blog
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.bloghome, name="home"),
    path('<str:slug>',views.blogPost, name="blogPost"),
]
