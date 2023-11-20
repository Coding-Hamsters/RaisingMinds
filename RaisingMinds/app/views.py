from django.shortcuts import render
from users.models import User
from user_profile.models import Profile
from django.contrib.auth.decorators import login_required
from post.models import Post
from school_profile.models import schoolProfile
from .models import Messages

# Create your views here.
def index(request):

    # get current authenticated user
    user = request.user
    # get all post in Post model
    post = Post.objects.all()
    
    try:
        # get the current user's profile
        profile = Profile.objects.get(user = request.user)
        # school_profile = schoolProfile.objects.get(user = request.user)

    except:
        profile = None
        # school_profile = None

    try:
        # get the current user's school profile
        school_profile = schoolProfile.objects.get(user = request.user)
        # school_profile = schoolProfile.objects.get(user = request.user)

    except:
        school_profile = None
        # school_profile = None

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # save the message to the database
        message = Messages.objects.create(name = name,email = email, subject = subject, message = message)
        message.save()

        

    return render(request,'app/index.html',{'user':user,'profile':profile,'navbar':'index','posts':post,'school_profile':school_profile})

def home(request):

    user = request.user

    return render(request,'app/home.html',{'user':user})


def project(request):

    user = request.user

    post = Post.objects.all()

    try:
        profile = Profile.objects.get(user = request.user)
    except:
        profile = None

    try:
        # get the current user's school profile
        school_profile = schoolProfile.objects.get(user = request.user)
        # school_profile = schoolProfile.objects.get(user = request.user)

    except:
        school_profile = None
        # school_profile = None

    return render(request,'app/projects.html',{'user':user,'profile':profile,'navbar':'projects','school_profile':school_profile,'posts':post})