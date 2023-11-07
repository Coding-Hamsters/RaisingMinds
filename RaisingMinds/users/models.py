from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.utils import timezone

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,email,username,password = None,**extra_fields):
        if not email:
            raise ValueError("email is required!")
        
        if not username:
            raise ValueError('username is required!')
        
        email = self.normalize_email(email)
        username = username

        user = self.model(email = email,username = username,**extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self,email,username,password = None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,username,password,**extra_fields)

    
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
