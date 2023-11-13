from django.shortcuts import render
from users.models import User
from user_profile.models import Profile

# Create your views here.
def index(request):

    user = request.user
    try:
        profile = Profile.objects.get(user = request.user)
    except:
        profile = None

    return render(request,'app/index.html',{'user':user,'profile':profile})

def home(request):

    user = request.user

    return render(request,'app/home.html',{'user':user})

def project(request):

    return render(request,'app/projects.html')