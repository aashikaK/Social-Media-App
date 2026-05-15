from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import Post
from .models import Like,Comment

# Create your views here.

@login_required
def deletePost(request,post_id):
    post= get_object_or_404(Post,id=post_id)
    if request.user == post.user:
        post.delete()
        messages.success(request, "Post deleted successfully.")

    return redirect('home')

@login_required
def likePost(request,post_id):
    post=get_object_or_404(Post,id=post_id) 
    like,created=Like.objects.get_or_create(user=request.user,post=post)

    if not created:
        like.delete()

    return redirect("home")

@login_required
def addComment(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    content=request.POST.get('content')

    if content:
        Comment.objects.create(
            user=request.user,
            post=post,
            content=content
        )
        messages.success(request, "Posted the comment successfully.")
    return redirect("home")

@login_required
def deleteComment(request,comment_id):
    comment= get_object_or_404(Comment,id=comment_id)
    if request.user!=comment.user:
        return redirect("home")
    comment.delete()
    messages.success(request, "Comment deleted.")
    return redirect("home")