from django.shortcuts import render
from user_profile.models import Profile

# Create your views here.
# method for render school_profile.html
def schoolprofile(request):

    user = request.user
    try:
        profile = Profile.objects.get(user = request.user)
    except:
        profile = None

    return render(request,'school_profile/school_profile.html',{'user':user,'profile':profile})
