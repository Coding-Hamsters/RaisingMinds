from django.db import models
from users.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100,null = True,blank=True)
    profile_image = models.ImageField(upload_to='profile_images',default='profile_images/defalt_profile_image.jpg')

    def __str__(self):
        return self.user.username
    
