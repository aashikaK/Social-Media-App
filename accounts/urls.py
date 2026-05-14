from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name="home"),
    path('login/', views.loginUser,name="login"),
    path('logout/', views.logoutUser,name="logout"),
    path('register/', views.registerUser,name="register"),
    path('profile/<str:username>/', views.profile, name="profile"),

]
