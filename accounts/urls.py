from django.contrib import admin,views
from django.urls import path

urlpatterns = [
    path('/', views.home,name="home"),
    path('login', views.loginUser,name="login"),
    path('logout', views.logoutser,name="logout"),

]
