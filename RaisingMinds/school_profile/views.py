from django.shortcuts import render,redirect
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

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        goal_donation = request.POST.get('goal_donation')
        post_img = request.FILES.get('post_img')

        new_post = Post.objects.create(author = school_profile,title = title,content = description,donate_amount = goal_donation,post_image = post_img)
        new_post.save()

        
    

    return render(request,'school_profile/school_profile.html',{'user':user,'profile':profile,'school_profile':school_profile,'posts':posts})
