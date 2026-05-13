from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:post_id>/', views.deletePost, name="delete_post"),

    path('like/<int:post_id>/', views.likePost, name="like_post"),
    path('comment/<int:post_id>/', views.addComment, name="add_comment"),
]