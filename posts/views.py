from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def createPost(request):
    if request.method=="POST":
        content= request.get.POST(content)

        Post.objects.create(
            user=request.user,
            content=content
        )
        redirect('home')
    redirect('home')
