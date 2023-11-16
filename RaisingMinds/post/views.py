from django.shortcuts import render
from user_profile.models import Profile
from school_profile.models import schoolProfile
from .models import Post

# Create your views here.
def community(request):

     # get current authenticated user
    user = request.user
    # get all post in Post model
    posts = Post.objects.all()
    
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

    return render(request,'post/community.html',{'user':user,'profile':profile,'navbar':'community','posts':posts,'school_profile':school_profile})
