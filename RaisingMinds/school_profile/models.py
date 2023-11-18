from django.db import models
from users.models import User
from django.utils import timezone

# Create your models here.
# build the schoolProfile model
class schoolProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    school_type = models.CharField(max_length=20,blank=True)
    Description = models.TextField(blank=True)
    principal_name = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.TextField()
    school_email = models.EmailField(blank=True)
    school_telephone = models.CharField(max_length=10,blank=True)
    verification_doc = models.FileField(upload_to='schoolProfile_vetification_documents')
    school_profile_img = models.ImageField(upload_to='schoolProfile_profile_images')
    date_created = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return self.school_name
    
