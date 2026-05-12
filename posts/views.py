from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def createPost(request):
    if request.method=="POST":
        content= request.POST.get("content")

        Post.objects.create(
            user=request.user,
            content=content
        )
        return redirect('home')
    return redirect('home')
