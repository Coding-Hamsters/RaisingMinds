from django.shortcuts import render,redirect
from django.http import HttpResponse
from user_profile.models import Profile
from .models import schoolProfile
from post.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
# method for render school_profile.html
@login_required(login_url='login')
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
        # filter posts creaed by current school profile
        posts = Post.objects.all().filter(author = school_profile)
    except:
        posts = None

    context = {
        'user':user,
        'profile':profile,
        'school_profile':school_profile,
        'posts':posts
    }

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        goal_donation = request.POST.get('goal_donation')
        post_img = request.FILES.get('post_img')

        # pass the variable into post model
        new_post = Post.objects.create(
            author = school_profile,
            title = title,
            content = description,
            donate_amount = goal_donation,
            post_image = post_img)
        
        # save the new post
        new_post.save()

        
    

    return render(request,'school_profile/school_profile.html',context)

# method for create new school profile
@login_required(login_url='login')
def createSchoolProfile(request):

    user = request.user
    try:
        # get current authenticated user's profile
        profile = Profile.objects.get(user = request.user)
    except:
        profile = None

    # try:
    #      # get current authenticated user's school profile pk
    #     school_profile = schoolProfile.objects.get()
    # except:
    #     school_profile = None

    try:
        # filter posts creaed by current school profile
        posts = Post.objects.all().filter(author = school_profile)
    except:
        posts = None

    context = {
        'user':user,
        'profile':profile,
        # 'school_profile':school_profile,
        'posts':posts
    }
    

    if request.method == 'POST':

        if schoolProfile.objects.filter(user = user).exists():
            return HttpResponse('<h1>You already have a school profile</h1>')

        schoolName = request.POST.get('schoolName')
        schoolPrincipalName = request.POST.get('principalName')
        schoolEmail = request.POST.get('schoolEmail')
        schoolProvince = request.POST.get('schoolProvince')
        schoolDistrict = request.POST.get('schoolDistrict')
        schoolTeleNo = request.POST.get('phoneNo')
        schoolType = request.POST.get('schoolType')
        schoolAddress = request.POST.get('schoolAddress')
        schoolDescription = request.POST.get('description')
        schoolVerificationDoc = request.FILES.get('verificationDoc')
        schoolProfileImage = request.FILES.get('schoolProfileImage')

        # create new school profile
        new_school_profile = schoolProfile.objects.create(
            user = user,
            school_name = schoolName,
            school_type = schoolType,
            Description = schoolDescription,
            principal_name = schoolPrincipalName,
            province = schoolProvince,
            district = schoolDistrict,
            address = schoolAddress,
            school_email = schoolEmail,
            school_telephone = schoolTeleNo,
            verification_doc = schoolVerificationDoc,
            school_profile_img = schoolProfileImage,
            # date_created = models.DateTimeField(default=timezone.now)
            # is_verified = models.BooleanField(default=True)
        )

        # save new school profile
        new_school_profile.save()

        return redirect('pendingschoolprofile')

    return render(request,'school_profile/school_registration.html',context)

# method for render pending school profile massage
@login_required(login_url='login')
def pendingSchoolProfile(request):

    return render(request,'school_profile/pending_school_profile.html')
