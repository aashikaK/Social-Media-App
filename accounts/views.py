from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from posts.models import Post
from accounts.models import Profile
from interactions.models import Like
# Create your views here.

#pw for ak is Ak123@ 

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

def registerUser(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        fullName = request.POST.get("full_name")
        dob = request.POST.get("dob")
        # password check
        if password != confirm_password:
            return render(request, "register.html", {
                "error": "Passwords do not match"
            })

        # username already exists
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already exists"
            })
        
        # email validation
        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {
            "error": "Email already exists"
            })
        
        try:
            validate_email(email)

        except ValidationError:
            return render(request, "register.html", {
                "error": "Enter a valid email address"
                })
        
        # password length
        if len(password) < 6:
            return render(request, "register.html", {
                "error": "Password must be at least 8 characters"
            })

        # uppercase check
        if not any(char.isupper() for char in password):
            return render(request, "register.html", {
                "error": "Password must contain an uppercase letter"
            })

        # lowercase check
        if not any(char.islower() for char in password):
            return render(request, "register.html", {
                "error": "Password must contain a lowercase letter"
            })

        # number check
        if not any(char.isdigit() for char in password):
            return render(request, "register.html", {
                "error": "Password must contain a number"
            })

        # special character check
        special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

        if not any(char in special_characters for char in password):
            return render(request, "register.html", {
                "error": "Password must contain a special character"
            })


        # create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        Profile.objects.create(
        user=user,
        full_name=fullName,
        dob=dob
        )

        user.save()

        return redirect("login")

    return render(request, "register.html")

# home page

def home(request):
    if request.user.is_anonymous:
        return redirect("login")
    posts=Post.objects.all().order_by("-created_at") #- means newest first
    liked_posts = Like.objects.filter(user=request.user).values_list('post_id', flat=True)

    return render(request, "home.html", {
    "posts": posts,
    "liked_posts": liked_posts
})


def profile(request,username):
    user=get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user).order_by("-created_at")
    profile=get_object_or_404(Profile,user=user)
    return render(request,"profile.html",{
        "profile_user":user,
        "profile": profile,
        "posts":posts
    })

@login_required
def editProfile(request):
    profile = request.user.profile

    if request.method == "POST":
        profile.full_name = request.POST.get("full_name")
        profile.dob = request.POST.get("dob")
        profile.bio = request.POST.get("bio")
        profile.save()

        return redirect("profile", username=request.user.username)

    return render(request, "edit_profile.html", {
        "profile": profile
    })

def logoutUser(request):
    logout(request)
    return redirect("login/")