from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def loginUser(request):
    if request.method == "POST":
        username= request.POST.get("username")
        password= request.POST.get("password")

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,"login.html",{
                "error": "Invalid username or password"
            })
    return render(request, "login.html")

def home(request):
    if request.user.is_anonymous:
        return redirect("login")

    return render(request, "home.html")

def logoutUser(request):
    logout(request)
    return redirect("login")