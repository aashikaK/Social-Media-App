from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


# Create your models here.
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE,related_name="comments")
    content=models.TextField()

    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return f"{self.user.username} - {self.content[:20]}"
    

class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name="likes")
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')