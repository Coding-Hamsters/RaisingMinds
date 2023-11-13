from django.shortcuts import render
from users.models import User
from user_profile.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    user = request.user
    try:
        profile = Profile.objects.get(user = request.user)
    except:
        profile = None

    return render(request,'app/index.html',{'user':user,'profile':profile,'navbar':'index'})

def home(request):

    user = request.user

    return render(request,'app/home.html',{'user':user})


def project(request):

    user = request.user
    try:
        profile = Profile.objects.get(user = request.user)
    except:
        profile = None

    return render(request,'app/projects.html',{'user':user,'profile':profile,'navbar':'projects'})