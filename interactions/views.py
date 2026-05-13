from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import Post

# Create your views here.

@login_required
def deletePost(request,post_id):
    post= get_object_or_404(Post,id=post_id)
    if request.user == post.user:
        post.delete()
        messages.success(request, "Post deleted successfully.")

    return redirect('home')