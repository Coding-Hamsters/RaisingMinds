from django.shortcuts import render
from school_profile.models import schoolProfile
from user_profile.models import Profile

# Create your views here.
def userProfile(request):

    user = request.user

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

    return render(request,'user_profile/user_profile.html',{'user':user,'school_profile':school_profile,'profile':profile})
