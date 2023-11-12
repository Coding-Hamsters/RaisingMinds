from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import login as user_login,logout as user_logout,authenticate
from user_profile.models import Profile

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from .token import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .helpers import send_forget_password_mail
import uuid

# Create your views here.
def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:

            if User.objects.filter(email = email).exists():
                return HttpResponse('<h1>Email is Already Exists</h1>')
            
            else:
                newUser = User.objects.create_user(email,username,password1)
                newUser.is_active = False
                newUser.save()

                # create user profile
                user_model = User.objects.get(email = email)
                new_profile = Profile.objects.create(user = user_model)
                new_profile.save()

                # set up email comfimation to signup
                current_site = get_current_site(request)
                subject = "Confirm Your Email"
                message = render_to_string('users/confirmationEmail.html',{
                    'user': newUser,
                    'domain':current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(newUser.pk)),
                    'token': generate_token.make_token(newUser)

                })

                email = EmailMessage(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [newUser.email]

                )

                email.send()

                return HttpResponse('<h1>We Send You a Confirmation Email</h1>')

    return render(request,'users/signup.html')

def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')

        user = authenticate(request,email = email,password = password1)   

        if user is not None:
            user_login(request,user)
            return redirect('index')
        
        else:
            return HttpResponse('<h1>Username or Password is invalid</h1>')

    return render(request,'users/login.html')

def logout(request):
    user_logout(request)
    return redirect('index')

# active the user after confirm the comfirmation mail
def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()

        user_login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('login')
    else:
        return HttpResponse('<h1>Activation Fail!</h1>')
    
    # change the password 
def ChangePassword(request,token):
    context = {}
    try:
        
        profile_obj = Profile.objects.filter(forget_password_token = token).first()
        context = {'user_id' : profile_obj.user.id}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change-password/{token}/')
                
            
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/change-password/{token}/')
                         
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('login')
        
    except Exception as e:
        print(e)
    return render(request,'users/change-password.html',context)

def ForgetPassword(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            
            if not User.objects.filter(email = email).first():
                messages.success(request, 'Not user found with this email.')
                return HttpResponse('<h1>Sent You a mail to reset password</h1>')
            
            user_obj = User.objects.get(email = email)
            token = str(uuid.uuid4())
            profile_obj= Profile.objects.get(user = user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email , token)
            messages.success(request, 'An email is sent.')
            return redirect('forget_password')
                
    
    
    except Exception as e:
        print(e)
    return render(request , 'users/forget-password.html')
