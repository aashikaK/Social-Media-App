from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:post_id>/', views.deletePost, name="delete_post"),
]