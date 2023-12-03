from django.shortcuts import render,redirect
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

    if request.method == 'POST':

        if request.FILES.get('image') == None:
            profile_image = profile.profile_image
            username = request.POST.get('username')

            profile.profile_image == profile_image
            user.username = username
            user.save()
            profile.save()

        if request.POST.get('username') == None:
            profile_image = request.FILES.get('image')
            username = user.username

            profile.profile_image = profile_image
            user.username = username
            user.save()
            profile.save()

        if request.FILES.get('image') != None:
            profile_image = request.FILES.get('image')
            username = request.POST.get('username')

            profile.profile_image = profile_image
            user.username = username
            user.save()
            profile.save()
        

    return render(request,'user_profile/user_profile.html',{'user':user,'school_profile':school_profile,'profile':profile})

def deleteUser(request,pk):

    user = request.user


    if request.method == 'POST':
        user = request.user
        print(user.username)

        redirect('login')

    return render(request,'user_profile/user_profile.html',{'user':user})
