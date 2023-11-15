from django.shortcuts import render
from user_profile.models import Profile
from .models import schoolProfile
from post.models import Post

# Create your views here.
# method for render school_profile.html
def schoolprofile(request,pk):

    # get current authenticated user
    user = request.user
    try:
        # get current authenticated user's profile
        profile = Profile.objects.get(user = request.user)
    except:
        profile = None

    try:
         # get current authenticated user's school profile pk
        school_profile = schoolProfile.objects.get(pk = pk)
    except:
        school_profile = None

    try:
        posts = Post.objects.all().filter(author = school_profile)
    except:
        posts = None

    return render(request,'school_profile/school_profile.html',{'user':user,'profile':profile,'school_profile':school_profile,'posts':posts})
