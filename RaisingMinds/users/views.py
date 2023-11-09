from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import login as user_login,logout,authenticate

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
                newUser.save()


    return render(request,'users/signup.html')

def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')

        user = authenticate(request,email = email,password = password1)   

        if user is not None:
            user_login(request,user)
            return redirect('home')
        
        else:
            return HttpResponse('<h1>Username or Password is invalid</h1>')

    return render(request,'users/login.html')

# def logout(request):
#     pass
